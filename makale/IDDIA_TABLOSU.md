# Makale iddia tablosu (Hafta 1 taslağı)

**Tek cümlelik katkı (geçici):** Across noisy 10-second windows from two MIT-BIH NSTDB ECG base recordings at 0, 6, and 24 dB, a paired F1 comparison of one R-peak detector on raw, Butterworth-filtered, and wavelet-thresholded signals found the highest point estimate with Butterworth preprocessing in all six variants.

Bu tablo yalnız mevcut NSTDB analizini anlatır. `118` ve `119` iki temel kayıttır; `e00`, `e06` ve `e24` bunların SNR sürümleridir. Altı sürüm altı bağımsız kişi değildir. Güven aralıkları kayıt içindeki eşleştirilmiş pencerelerin 1.000 bootstrap tekrarına dayanır.

| İddia | Kanıt | Şekil ya da tablo | Durum |
|---|---|---|---|
| 118e24 kaydının gürültülü pencerelerinde Butterworth, ham baseline F1 değerini artırdı. | Ham F1 0,946; Butterworth F1 0,997; eşleştirilmiş fark 0,051 (%95 GA 0,041–0,061). | [F1 ve %95 GA grafiği](../nstdb_3_yontem_f1_ga95.png); [README sonuç tablosu](../README.md#sonuçlar) | Var |
| Butterworth, altı sürümün tamamında en yüksek havuzlanmış F1 nokta tahminini verdi. | Butterworth F1: 118e00 0,620; 118e06 0,734; 118e24 0,997; 119e00 0,576; 119e06 0,706; 119e24 0,946. Aynı kayıtların ham ve dalgacık değerleri README tablosundadır. | [F1 ve %95 GA grafiği](../nstdb_3_yontem_f1_ga95.png); [README sonuç tablosu](../README.md#sonuçlar) | Var |
| Bu ayarlarda dalgacık eşikleme, ham baseline üzerinde her sürümde iyileşme sağlamadı. | 118e00: ham 0,543, dalgacık 0,540; 119e00: ham 0,543, dalgacık 0,546. | [F1 ve %95 GA grafiği](../nstdb_3_yontem_f1_ga95.png) | Var |
| Sonuçların bağımsız kişilere genellenebilirliği gösterilecek. | Mevcut analizde yalnız iki temel kayıt ve kayıt içi pencere bootstrap'i var. Bağımsız kayıtlarla kişi bazlı test henüz yapılmadı. | Planlanan kişi bazlı test tablosu | Yapılacak |

## Açık işler

- Hedef dergide son iki yılda yayımlanan üç yakın makalenin gerçek katkısını okuyup karşılaştırmak. Bu yapılmadan yenilik veya makale kabulü iddiası kurulmaz.
- En az üç tekrar ve bağımsız kişi/kayıt bazlı test düzenini belirleyip uygulamak; test pencerelerine bakarak parametre seçmemek.
- Şekil ve tablo adlarını son makale iskeletiyle eşleştirmek.

**Kaynak veri:** [MIT-BIH Noise Stress Test Database](https://physionet.org/content/nstdb/1.0.0/). Ham sinyal dosyaları bu depoda tutulmaz.
