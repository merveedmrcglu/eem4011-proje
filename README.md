# NSTDB'de R Tepesi Tespiti

Bu projede NSTDB EKG kayıtlarında R tepesi tespiti, ham sinyal ile Butterworth filtresi uygulanmış sinyalde karşılaştırılır.

## Veri seti

MIT-BIH Noise Stress Test Database (NSTDB), PhysioNet:  
https://physionet.org/content/nstdb/1.0.0/

Kullanılan kayıtlar: `118e24` ve `118e00`. Veriler Colab'de WFDB ile PhysioNet'ten okunur; veri dosyaları bu depoya eklenmemiştir.

## Colab'de çalıştırma

1. Notebook'u Google Colab'de açın.
2. `wfdb`, `scipy`, `numpy` ve `matplotlib` kütüphanelerini yükleyin.
3. Notebook hücrelerini sırayla çalıştırın. Kod, kayıtları WFDB üzerinden PhysioNet'ten okur.
4. Ham sinyal ve 5–20 Hz Butterworth band-pass filtreli sinyalde aynı tepe bulma ve değerlendirme adımlarını çalıştırın.

## Şekiller

- Ham EKG sinyali üzerinde referans ve bulunan tepelerin karşılaştırması.
- Ham sinyal ile Butterworth filtreli sinyalde bulunan tepelerin karşılaştırması.

## İlk sonuçlar

- `118e24` tam kaydı: ham sinyal F1 = **0.971**, Butterworth sonrası F1 = **0.998**.
- `118e00` gürültülü bölümleri: ham sinyal F1 değerleri **0.490–0.646**, Butterworth sonrası **0.539–0.767** aralığında ölçüldü.

Bunlar ilk deneme sonuçlarıdır; henüz nihai sonuç değildir.

## Atıf ve lisans

Moody GB, Muldrow WE, Mark RG. “A noise stress test for arrhythmia detectors.” *Computers in Cardiology*, 1984; 11:381–384.

NSTDB lisansı: Open Data Commons Attribution License v1.0.  
Kaynak ve lisans: https://physionet.org/content/nstdb/1.0.0/
