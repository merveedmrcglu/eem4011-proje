# Bağımsız temel kayıtlarda ek test protokolü

Bu protokol sonuçlar hesaplanmadan önce sabitlenmiştir. Test, önceki NSTDB 118/119 tablosunun yerine geçmez.

- Kaynak: PhysioNet MIT-BIH Arrhythmia Database (`mitdb`) kayıtları **100, 101, 103, 105** ve MIT-BIH Noise Stress Test Database (`nstdb`) `em` elektrot hareketi gürültüsü. Bu dört temel EKG, önceki NSTDB 118/119 temel kayıtlarından farklıdır.
- Her temiz EKG ve `em` gürültüsü için 300–900 saniyelik birinci kanal kesiti, 360 Hz. Her EKG'ye aynı gürültü kesiti ayrı ayrı **0, 6, 24 dB** hedef SNR ile eklenir. Gürültünün ortalaması çıkarılır; ölçek, her EKG kesitinin merkezlenmiş RMS değerinden hesaplanır. Bu, doğal bir yeni hasta kaydı değil, sentetik stres testidir.
- Her kayıt ve SNR için 60 adet örtüşmeyen 10 saniyelik pencere. Her pencerenin iki ucundaki 150 ms değerlendirme dışı. Referanslar yalnız WFDB `atr` atım simgeleri; ritim/not işaretleri hariç.
- Ham `find_peaks`, sıfır fazlı dördüncü derece 5–20 Hz Butterworth ve `sym4` 8 seviyeli evrensel yumuşak eşikleme. Her üçünde `find_peaks(distance=0.30*fs, prominence=0.5)`; referansla bire bir eşleştirme ±150 ms. Parametreler NSTDB 118/119 testinden sonra değiştirilmez.
- Çıktı: kişi/kayıt ve SNR başına TP, FP, FN, F1; ayrıca dört kaydın toplam olay sayılarıyla havuzlanmış F1. Kişiler arası n=4 küçük olduğundan güven aralığı veya nüfus genellemesi iddia edilmez. Aynı `em` gürültü kesiti tekrar kullanıldığı için gürültü örneği bağımsızlığı yoktur.
- Tekrarlanabilirlik: `python makale/dis_dogrulama.py` komutu, `wfdb`, `numpy`, `scipy`, `PyWavelets`, `matplotlib` kurulu ortamda PhysioNet'ten kayıtları okur ve CSV/PNG üretir. Ham veri depoya yüklenmez.
