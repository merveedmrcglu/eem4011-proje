# NSTDB'de R Tepesi Tespiti

Bu projede MIT-BIH Noise Stress Test Database (NSTDB) EKG kayıtlarında R tepesi tespiti, ham sinyal ve Butterworth band-pass filtresi uygulanmış sinyal üzerinde karşılaştırılır.

## Veri seti

Veri seti: [MIT-BIH Noise Stress Test Database (NSTDB)](https://physionet.org/content/nstdb/1.0.0/)

Kullanılan kayıtlar `118e24` ve `118e00`'dır. Kayıtlar Colab'de WFDB kütüphanesi aracılığıyla PhysioNet'ten okunur. Veri dosyaları bu depoya eklenmemiştir.

## Colab'de çalıştırma

1. Notebook'u Google Colab'de açın.
2. `wfdb`, `scipy`, `numpy` ve `matplotlib` kütüphanelerinin kullanılabilir olduğunu doğrulayın.
3. Notebook hücrelerini sırayla çalıştırın. Kod, kayıtları WFDB üzerinden PhysioNet'ten okur.
4. Ham sinyal ve 5–20 Hz Butterworth band-pass filtreli sinyal için tepe bulma ve değerlendirme adımlarını çalıştırın.

## Şekiller

- Ham EKG sinyali üzerinde referans atımların ve bulunan tepelerin karşılaştırması.
- Ham ve Butterworth filtreli sinyallerde bulunan tepelerin karşılaştırması.

## İlk sonuçlar

- `118e24` kaydının tamamında F1: ham sinyal **0.971**, Butterworth sonrası **0.998**.
- `118e00` kaydının analiz edilen gürültülü bölümlerinde F1 aralığı: ham sinyal **0.490–0.646**, Butterworth sonrası **0.539–0.767**.

Bunlar iki kayıt üzerinde elde edilen ilk sonuçlardır; nihai sonuç olarak değerlendirilmemelidir.

## Atıf ve lisans

Moody GB, Muldrow WE, Mark RG. “A noise stress test for arrhythmia detectors.” *Computers in Cardiology*, 1984; 11:381–384.

NSTDB, [Open Data Commons Attribution License v1.0](https://physionet.org/content/nstdb/1.0.0/) koşullarıyla sunulmaktadır.
