# NSTDB EKG kayıtlarında R tepesi tespiti

Bu projede elektrot hareketi gürültüsü içeren EKG kayıtlarında üç R tepesi tespit yaklaşımı karşılaştırılır: ham sinyalde find_peaks taban çizgisi, Butterworth bant geçiren filtre ve dalgacık eşikleme.

## Problem ve amaç

Elektrot hareketi artefaktı EKG'de kalp atımına benzeyen biçimler oluşturabilir. Bu nedenle gürültü altında R tepelerinin kaçırılması veya yanlış tepe işaretlenmesi artabilir. Amaç, aynı referans atımlar ve aynı değerlendirme koşullarıyla üç yöntemin performansını karşılaştırmaktır.

## Veri seti ve kapsam

[MIT-BIH Noise Stress Test Database (NSTDB)](https://physionet.org/content/nstdb/1.0.0/) kullanıldı. Temiz 118 ve 119 EKG kayıtlarının elektrot hareketi gürültüsü eklenmiş şu altı sürümü incelendi: 118e00, 118e06, 118e24, 119e00, 119e06 ve 119e24. Sonekler sırasıyla 0, 6 ve 24 dB SNR düzeylerini belirtir. Örnekleme frekansı 360 Hz'dir. Her kayıt için gürültülü kısımlardan 78 adet eşleştirilmiş 10 saniyelik pencere değerlendirildi; ilk beş dakikalık temiz kısım bu gürültülü pencere analizine alınmadı.

Ham NSTDB sinyal dosyaları bu depoya eklenmemiştir; kayıtlar WFDB aracılığıyla PhysioNet'ten okunur.

## Yöntem

- **Ham sinyal (baseline):** SciPy find_peaks; en az 0,30 saniye tepe aralığı ve 0,5 prominence.
- **Butterworth:** 4. derece, 5–20 Hz bant geçiren filtre; ileri-geri filtreleme ve aynı tepe bulucu.
- **Dalgacık:** sym4 dalgacığıyla 8 seviyeli ayrıştırma ve eşikleme.
- **Değerlendirme:** Referans anotasyonlarla bulunan tepeler bire bir eşleştirildi; ±150 ms toleransla F1 hesaplandı.
- **Belirsizlik:** Her kayıt için 78 pencere eşleştirilerek 1000 tekrarlı pencere bootstrap'iyle %95 güven aralığı (GA) hesaplandı. Bu aralık kayıt içindeki pencerelerin değişkenliğini gösterir; bağımsız kişiler arası belirsizliği ölçmez.

## Sonuçlar

Tabloda her yöntemin havuzlanmış F1 değeri ve pencere bootstrap'iyle hesaplanan %95 GA'sı verilir.

| Kayıt | SNR (dB) | Ham F1 (%95 GA) | Butterworth F1 (%95 GA) | Dalgacık F1 (%95 GA) |
|---|---:|---:|---:|---:|
| 118e00 | 0 | 0,543 (0,522–0,563) | 0,620 (0,599–0,641) | 0,540 (0,520–0,559) |
| 118e06 | 6 | 0,605 (0,579–0,632) | 0,734 (0,713–0,755) | 0,608 (0,581–0,636) |
| 118e24 | 24 | 0,946 (0,935–0,956) | 0,997 (0,994–0,999) | 0,962 (0,953–0,971) |
| 119e00 | 0 | 0,543 (0,523–0,564) | 0,576 (0,556–0,597) | 0,546 (0,526–0,568) |
| 119e06 | 6 | 0,648 (0,626–0,670) | 0,706 (0,690–0,723) | 0,652 (0,629–0,675) |
| 119e24 | 24 | 0,839 (0,823–0,855) | 0,946 (0,933–0,959) | 0,857 (0,840–0,874) |

Butterworth yöntemi altı kaydın tamamında en yüksek havuzlanmış F1 nokta tahminini verdi. Dalgacık yöntemi ham baseline'a yakın sonuçlar verdi; bu analiz, dalgacığın her kayıtta iyileşme sağladığını göstermiyor. Sonuçlar yalnızca incelenen altı kayıt ve gürültülü pencereler için geçerlidir.

## Grafikler

- [Altı kayıtta üç yöntemin F1 ve %95 GA karşılaştırması](jury-figures/nstdb_3_yontem_f1_ga95.png)
- [118e00: en düşük ham F1 pencereleri](jury-figures/118e00_en_dusuk_ham_f1_3_yontem.png)
- [118e06: en düşük ham F1 pencereleri](jury-figures/118e06_en_dusuk_ham_f1_3_yontem.png)
- [118e24: en düşük ham F1 pencereleri](jury-figures/118e24_en_dusuk_ham_f1_3_yontem.png)
- [119e00: en düşük ham F1 pencereleri](jury-figures/119e00_en_dusuk_ham_f1_3_yontem.png)
- [119e06: en düşük ham F1 pencereleri](jury-figures/119e06_en_dusuk_ham_f1_3_yontem.png)
- [119e24: en düşük ham F1 pencereleri](jury-figures/119e24_en_dusuk_ham_f1_3_yontem.png)

## Sınırlılıklar

118 ve 119, NSTDB'de gürültü eklenmiş iki temel EKG kaydının farklı SNR sürümleridir; altı sürüm altı bağımsız kişi anlamına gelmez. Bootstrap yalnızca her kaydın pencereleri içinde yapılmıştır. Bu nedenle sonuçlar daha geniş bir hasta grubuna genellenemez.

## Kod

[Google Colab analiz defteri](NSTDB_R_Tepesi_Tespiti_Analiz.ipynb)

## Kaynak ve lisans

Moody GB, Muldrow WE, Mark RG. “A noise stress test for arrhythmia detectors.” *Computers in Cardiology*, 1984; 11:381–384. NSTDB, [Open Data Commons Attribution License v1.0](https://physionet.org/content/nstdb/1.0.0/) koşullarıyla sunulur.
