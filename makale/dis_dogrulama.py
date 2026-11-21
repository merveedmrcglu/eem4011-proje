"""Fixed-parameter external-base-record stress test; see DIS_DOGRULAMA_PROTOKOLU.md."""

from pathlib import Path
import csv

import numpy as np
import pywt
import wfdb
from scipy.signal import butter, find_peaks, sosfiltfilt


RECORDS = ("100", "101", "103", "105")
SNRS_DB = (0, 6, 24)
BEAT_SYMBOLS = set("NLRBAaJSVrFejnE/fQ?")
START_S, END_S, WINDOW_S = 300, 900, 10
TOL_S, DISTANCE_S, PROMINENCE = 0.15, 0.30, 0.5
OUTPUT = Path(__file__).resolve().parent


def wavelet_denoise(x):
    wavelet = pywt.Wavelet("sym4")
    level = min(8, pywt.dwt_max_level(len(x), wavelet.dec_len))
    coeffs = pywt.wavedec(x, wavelet, mode="symmetric", level=level)
    detail = coeffs[-1]
    sigma = np.median(np.abs(detail - np.median(detail))) / 0.6745
    threshold = sigma * np.sqrt(2 * np.log(len(x)))
    coeffs = [coeffs[0]] + [pywt.threshold(c, threshold, mode="soft") for c in coeffs[1:]]
    return pywt.waverec(coeffs, wavelet, mode="symmetric")[: len(x)]


def score(references, detections, tol):
    """One-to-one nearest available match, following the original notebook."""
    detections = np.sort(np.asarray(detections, dtype=int))
    used = np.zeros(len(detections), dtype=bool)
    tp = 0
    for ref in references:
        lo = np.searchsorted(detections, ref - tol)
        hi = np.searchsorted(detections, ref + tol, side="right")
        choices = np.arange(lo, hi)
        choices = choices[~used[choices]]
        if len(choices):
            best = choices[np.argmin(np.abs(detections[choices] - ref))]
            used[best] = True
            tp += 1
    return tp, len(detections) - tp, len(references) - tp


def f1(tp, fp, fn):
    denom = 2 * tp + fp + fn
    return 2 * tp / denom if denom else float("nan")


def main():
    fs = 360
    start, end = START_S * fs, END_S * fs
    noise_record = wfdb.rdrecord("em", pn_dir="nstdb", sampfrom=start, sampto=end)
    assert noise_record.fs == fs
    noise = np.asarray(noise_record.p_signal[:, 0], dtype=float)
    noise -= np.mean(noise)
    noise_rms = np.sqrt(np.mean(noise**2))
    assert noise_rms > 0
    tol, distance = round(TOL_S * fs), round(DISTANCE_S * fs)
    sos = butter(4, (5, 20), btype="bandpass", fs=fs, output="sos")
    rows = []
    for record_name in RECORDS:
        rec = wfdb.rdrecord(record_name, pn_dir="mitdb", sampfrom=start, sampto=end)
        ann = wfdb.rdann(record_name, "atr", pn_dir="mitdb", sampfrom=start, sampto=end)
        assert rec.fs == fs and rec.sig_name[0] == "MLII", (record_name, rec.sig_name)
        clean = np.asarray(rec.p_signal[:, 0], dtype=float)
        clean_rms = np.sqrt(np.mean((clean - np.mean(clean)) ** 2))
        refs = np.asarray([int(s) - start for s, symbol in zip(ann.sample, ann.symbol)
                           if symbol in BEAT_SYMBOLS], dtype=int)
        for snr_db in SNRS_DB:
            scale = clean_rms / (noise_rms * 10 ** (snr_db / 20))
            signal = clean + scale * noise
            signals = {
                "Ham": signal,
                "Butterworth": sosfiltfilt(sos, signal),
                "Dalgacik": wavelet_denoise(signal),
            }
            peaks = {method: find_peaks(s, distance=distance, prominence=PROMINENCE)[0]
                     for method, s in signals.items()}
            for window in range((END_S - START_S) // WINDOW_S):
                lo, hi = window * WINDOW_S * fs + tol, (window + 1) * WINDOW_S * fs - tol
                window_refs = refs[(refs >= lo) & (refs < hi)]
                for method, detections in peaks.items():
                    window_peaks = detections[(detections >= lo) & (detections < hi)]
                    tp, fp, fn = score(window_refs, window_peaks, tol)
                    rows.append({"kayit": record_name, "snr_db": snr_db,
                                 "pencere_baslangic_s": START_S + window * WINDOW_S,
                                 "yontem": method, "TP": tp, "FP": fp, "FN": fn,
                                 "F1": f1(tp, fp, fn)})

    window_path = OUTPUT / "dis_dogrulama_pencere.csv"
    with window_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)

    summary = []
    for record_name in (*RECORDS, "TOPLAM"):
        for snr_db in SNRS_DB:
            for method in ("Ham", "Butterworth", "Dalgacik"):
                subset = [r for r in rows if r["snr_db"] == snr_db and r["yontem"] == method
                          and (record_name == "TOPLAM" or r["kayit"] == record_name)]
                tp, fp, fn = (sum(r[k] for r in subset) for k in ("TP", "FP", "FN"))
                summary.append({"kayit": record_name, "snr_db": snr_db, "yontem": method,
                                "pencere": len(subset), "TP": tp, "FP": fp, "FN": fn,
                                "F1": f1(tp, fp, fn)})
    summary_path = OUTPUT / "dis_dogrulama_ozet.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=summary[0])
        writer.writeheader()
        writer.writerows(summary)

    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.6), sharey=True)
    colors = {"Ham": "#666666", "Butterworth": "#007f5f", "Dalgacik": "#b544a0"}
    for ax, snr_db in zip(axes, SNRS_DB):
        for method in colors:
            vals = [next(r["F1"] for r in summary if r["kayit"] == record and
                         r["snr_db"] == snr_db and r["yontem"] == method) for record in RECORDS]
            ax.plot(RECORDS, vals, marker="o", label=method, color=colors[method])
        ax.set_title(f"Sentetik em gürültüsü, {snr_db} dB")
        ax.set_xlabel("MIT-BIH temel kaydı")
        ax.grid(alpha=0.25)
    axes[0].set_ylabel("Havuzlanmış F1 (kayıt içi 60 pencere)")
    axes[-1].legend(loc="lower right", fontsize=8)
    fig.tight_layout()
    fig.savefig(OUTPUT / "dis_dogrulama_f1.png", dpi=180)
    plt.close(fig)
    for row in summary:
        if row["kayit"] == "TOPLAM":
            print(row)
    print("Kaydedildi:", window_path, summary_path)


if __name__ == "__main__":
    main()
