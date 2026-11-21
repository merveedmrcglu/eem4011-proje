# Makale iddia tablosu (Hafta 1 taslağı)

**Tek cümlelik katkı (geçici):** Across noisy 10-second windows from two MIT-BIH NSTDB ECG base recordings at 0, 6, and 24 dB, a paired F1 comparison of one R-peak detector on raw, Butterworth-filtered, and wavelet-thresholded signals found the highest point estimate with Butterworth preprocessing in all six variants.

Bu tablo yalnız mevcut NSTDB analizini anlatır. `118` ve `119` iki temel kayıttır; `e00`, `e06` ve `e24` bunların SNR sürümleridir. Altı sürüm altı bağımsız kişi değildir. Güven aralıkları kayıt içindeki eşleştirilmiş pencerelerin 1.000 bootstrap tekrarına dayanır.

| İddia | Kanıt | Şekil ya da tablo | Durum |
|---|---|---|---|
| 118e24 kaydının gürültülü pencerelerinde Butterworth, ham baseline F1 değerini artırdı. | Ham F1 0,946; Butterworth F1 0,997; eşleştirilmiş fark 0,051 (%95 GA 0,041–0,061). | [F1 ve %95 GA grafiği](../nstdb_3_yontem_f1_ga95.png); [README sonuç tablosu](../README.md#sonuçlar) | Var |
| Butterworth, altı sürümün tamamında en yüksek havuzlanmış F1 nokta tahminini verdi. | Butterworth F1: 118e00 0,620; 118e06 0,734; 118e24 0,997; 119e00 0,576; 119e06 0,706; 119e24 0,946. Aynı kayıtların ham ve dalgacık değerleri README tablosundadır. | [F1 ve %95 GA grafiği](../nstdb_3_yontem_f1_ga95.png); [README sonuç tablosu](../README.md#sonuçlar) | Var |
| Bu ayarlarda dalgacık eşikleme, ham baseline üzerinde her sürümde iyileşme sağlamadı. | 118e00: ham 0,543, dalgacık 0,540; 119e00: ham 0,543, dalgacık 0,546. | [F1 ve %95 GA grafiği](../nstdb_3_yontem_f1_ga95.png) | Var |
| Sonuçların bağımsız kişilere genellenebilirliği gösterilecek. | Mevcut analizde yalnız iki temel kayıt ve kayıt içi pencere bootstrap'i var. Bağımsız kayıtlarla kişi bazlı test henüz yapılmadı. | Planlanan kişi bazlı test tablosu | Yapılacak |

## Hedef dergideki yakın çalışmalarla katkı karşılaştırması

Aşağıdaki karşılaştırma yayınevinin makale sayfalarında erişilebilen metinlere dayanır. Rahman ve ark. için özet ve öne çıkanlar, Sanz-Guerrero ve ark. için açık tam HTML metin, Costabile ve ark. için yayınevi ön izlemesi ile indekslenmiş tam HTML bölümleri incelendi. Üç PDF'nin indirildiği iddia edilmez.

| Makale | Yayımlanmış katkısı | Bu projeye göre durum |
|---|---|---|
| [Rahman ve ark. (2025), *Impact and mitigation of blind filtering in automatic ECG analysis for wearable sensors*](https://doi.org/10.1016/j.bspc.2025.108294) | Derin öğrenme tabanlı gürültü algılayıcısı ile gürültülü bölümü dışlayan bir sistem öneriyor; aritmi sınıflandırması ve giyilebilir sensör/telefon deneyi raporluyor. | Sonuç ölçütü R tepesi F1 değil; burada sabit üç ön işlem yalnız iki temel NSTDB kaydında karşılaştırılıyor. **Kaynak kapsamı:** yayınevi özeti ve highlights. |
| [Sanz-Guerrero ve ark. (2026), *Peak Attention U-Net: Enhancing ECG delineation with attention*](https://doi.org/10.1016/j.bspc.2026.109874) | Dikkat kapılı 1D U-Net öneriyor; LUDB'deki 200 adet 12 derivasyonlu kaydı kayıt düzeyinde eğitim/doğrulama/teste ayırıp P, QRS ve T sınırları ile tepeleri ölçüyor. | Bu çalışmada model eğitimi veya bağımsız kayıt testi yok; yalnız tek kanallı R tepesi ölçülüyor. LUDB sonucu, farklı veri ve görev olduğu için doğrudan F1 kıyası değildir. **Kaynak kapsamı:** açık tam HTML metin. |
| [Costabile ve ark. (2026), *Pre-filtering ECG signals using the parabolic moving average to boost denoising performance*](https://doi.org/10.1016/j.bspc.2026.109788) | (1,4,1)/6 ağırlıklı üç örnekli PMA ön süzmesini önerip Savitzky–Golay, median, Butterworth ve ikinci dereceden yumuşatma ile iki sentetik, bir gerçek gürültülü EKG'de MSE, SNR ve PRD ölçüyor. | Bu proje yeni süzgeç önermiyor ve R tepesi F1 kullanıyor; Costabile'nin sinyal iyileştirme metrikleriyle doğrudan sayısal kıyas kurulamaz. **Kaynak kapsamı:** yayınevi ön izlemesi ve indekslenmiş HTML bölümleri; PDF erişimi sınırlı. |

**Düzey değerlendirmesi:** Mevcut çalışma karşılaştırmalı bir ön çalışmadır. Bu üç makalenin yöntem geliştirme ve doğrulama düzeyine henüz ulaşmaz; makale kabulü veya bağımsız hastalara genellenebilirlik iddiası kurulmaz.

## Açık işler

- Rahman ve Costabile makalelerinin erişim izinleri elverirse tam PDF'lerini okuyup karşılaştırmayı genişletmek. Şu anki karşılaştırmada erişim düzeyi yukarıda belirtilmiştir.
- En az üç tekrar ve bağımsız kişi/kayıt bazlı test düzenini belirleyip uygulamak; test pencerelerine bakarak parametre seçmemek.
- Şekil ve tablo adlarını son makale iskeletiyle eşleştirmek.

**Kaynak veri:** [MIT-BIH Noise Stress Test Database](https://physionet.org/content/nstdb/1.0.0/). Ham sinyal dosyaları bu depoda tutulmaz.
