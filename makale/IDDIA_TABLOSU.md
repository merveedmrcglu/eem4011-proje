# Makale iddia tablosu (Hafta 1 taslağı)

**Tek cümlelik katkı (geçici):** With fixed R-peak detector settings, paired F1 comparisons on six NSTDB noise variants and a separate four-record synthetic electrode-motion stress test found the highest pooled point estimate with Butterworth preprocessing at each tested SNR, while individual-record exceptions remained.

İlk üç sonuç NSTDB analizine, dördüncü sonuç ayrı bir sentetik gürültü stres testine dayanır. `118` ve `119` iki temel kayıttır; `e00`, `e06` ve `e24` bunların SNR sürümleridir. Altı sürüm altı bağımsız kişi değildir. Güven aralıkları kayıt içindeki eşleştirilmiş pencerelerin 1.000 bootstrap tekrarına dayanır.

| İddia | Kanıt | Şekil ya da tablo | Durum |
|---|---|---|---|
| 118e24 kaydının gürültülü pencerelerinde Butterworth, ham baseline F1 değerini artırdı. | Ham F1 0,946; Butterworth F1 0,997; eşleştirilmiş fark 0,051 (%95 GA 0,041–0,061). | [F1 ve %95 GA grafiği](../nstdb_3_yontem_f1_ga95.png); [README sonuç tablosu](../README.md#sonuçlar) | Var |
| Butterworth, altı sürümün tamamında en yüksek havuzlanmış F1 nokta tahminini verdi. | Butterworth F1: 118e00 0,620; 118e06 0,734; 118e24 0,997; 119e00 0,576; 119e06 0,706; 119e24 0,946. Aynı kayıtların ham ve dalgacık değerleri README tablosundadır. | [F1 ve %95 GA grafiği](../nstdb_3_yontem_f1_ga95.png); [README sonuç tablosu](../README.md#sonuçlar) | Var |
| Bu ayarlarda dalgacık eşikleme, ham baseline üzerinde her sürümde iyileşme sağlamadı. | 118e00: ham 0,543, dalgacık 0,540; 119e00: ham 0,543, dalgacık 0,546. | [F1 ve %95 GA grafiği](../nstdb_3_yontem_f1_ga95.png) | Var |
| NSTDB 118/119 dışında dört temel EKG'de, sentetik elektrot hareketi gürültüsü altında, Butterworth havuzlanmış F1 nokta tahmini üç SNR'de en yüksekti. | 0 dB: ham 0,866, Butterworth 0,901, dalgacık 0,876; 6 dB: 0,939/0,967/0,953; 24 dB: 0,997/0,999/0,998. 103 kaydının 6 dB sonucunda dalgacık 0,938 > Butterworth 0,929. | [Dış test protokolü](DIS_DOGRULAMA_PROTOKOLU.md), [kod](dis_dogrulama.py), [özet CSV](dis_dogrulama_ozet.csv), [grafik](dis_dogrulama_f1.png) | Var; sentetik gürültü, dört kişi |
| Sonuçların daha geniş ve doğal koşullarda gürültülü hasta grubuna genellenebilirliği gösterilecek. | Dört ayrı temel EKG'de sentetik stres testi var; aynı `em` gürültü kesiti tekrarlandı. Doğal gürültülü yeni kişi verisi ve geniş örneklem yok. | İleride planlanan doğal koşul testi | Yapılacak |

## Hedef dergideki yakın çalışmalarla katkı karşılaştırması

Aşağıdaki karşılaştırma kaynakların erişilebilen metinlerine dayanır. Rahman ve ark. makalesinin 9 sayfalık tam PDF'i kurumsal Figshare kaydından indirildi ve yöntem, sonuç, tartışma, sınırlılık bölümleri okundu. Sanz-Guerrero ve ark. için açık tam HTML metin, Costabile ve ark. için yayınevi ön izlemesi ve indekslenmiş HTML bölümleri incelendi. Son iki PDF indirilmedi. Ayrıca hedef dergiden iki farklı makalenin yazar ön baskısı indirilip incelendi; bunların konuları doğrudan gürültülü R tepesi tespiti olmadığı için yakın üçlüyle karıştırılmamalı. Ayrıntı [okuma kaydında](LITERATUR_OKUMA_KAYDI.md).

| Makale | Yayımlanmış katkısı | Bu projeye göre durum |
|---|---|---|
| [Rahman ve ark. (2025), *Impact and mitigation of blind filtering in automatic ECG analysis for wearable sensors*](https://doi.org/10.1016/j.bspc.2025.108294) | Altı açık veri kümesinde gürültü algılayıcısı için veri kümesi dışarıda bırakmalı değerlendirme kullanıyor; öğrenilmiş gürültü tespit ve dışlama yaklaşımını aritmi sınıflandırması ile giyilebilir sensör/telefon üzerinde inceliyor. Makalenin kendi sınırlılığı: gürültülü bölümleri atmak yararlı bilgi kaybettirebilir ve yöntem tek derivasyonla sınırlı. | Bu çalışmanın sonucu **R tepesi F1**; Rahman'ın F1'i **aritmi sınıflandırmasına** ait olduğundan sayısal kıyas yapılamaz. Burada dış veri kümesi ve cihaz testi yok. **Kaynak kapsamı:** [kurumsal Figshare tam PDF](https://figshare.com/articles/journal_contribution/Impact_and_mitigation_of_blind_filtering_in_automatic_ECG_analysis_for_wearable_sensors/29653379), 9 sayfa, okundu. |
| [Sanz-Guerrero ve ark. (2026), *Peak Attention U-Net: Enhancing ECG delineation with attention*](https://doi.org/10.1016/j.bspc.2026.109874) | Dikkat kapılı 1D U-Net öneriyor; LUDB'deki 200 adet 12 derivasyonlu kaydı kayıt düzeyinde eğitim/doğrulama/teste ayırıp P, QRS ve T sınırları ile tepeleri ölçüyor. | Bu çalışmada model eğitimi yok; tek kanallı R tepesi ölçülüyor. Dört ayrı temel EKG üzerinde sentetik gürültü stres testi yapıldı, fakat LUDB sonucu farklı veri ve görev olduğu için doğrudan F1 kıyası değildir. **Kaynak kapsamı:** açık tam HTML metin. |
| [Costabile ve ark. (2026), *Pre-filtering ECG signals using the parabolic moving average to boost denoising performance*](https://doi.org/10.1016/j.bspc.2026.109788) | (1,4,1)/6 ağırlıklı üç örnekli PMA ön süzmesini önerip Savitzky–Golay, median, Butterworth ve ikinci dereceden yumuşatma ile iki sentetik, bir gerçek gürültülü EKG'de MSE, SNR ve PRD ölçüyor. | Bu proje yeni süzgeç önermiyor ve R tepesi F1 kullanıyor; Costabile'nin sinyal iyileştirme metrikleriyle doğrudan sayısal kıyas kurulamaz. **Kaynak kapsamı:** yayınevi ön izlemesi ve indekslenmiş HTML bölümleri; PDF erişimi sınırlı. |

**Düzey değerlendirmesi:** Mevcut çalışma karşılaştırmalı bir ön çalışmadır. Bu üç makalenin yöntem geliştirme ve doğrulama düzeyine henüz ulaşmaz; makale kabulü veya bağımsız hastalara genellenebilirlik iddiası kurulmaz.

## Açık işler

- Sanz-Guerrero makalesinin açık erişimli PDF'ini ve Costabile makalesinin erişim izinleri elverirse tam PDF'ini edinip ayrıntılı okumak. Şu anki erişim düzeyi yukarıda belirtilmiştir.
- Dört farklı temel kayıtla yapılan ek sentetik gürültü stres testini daha geniş, doğal gürültülü bağımsız kişi verisiyle genişletmek; test pencerelerine bakarak parametre seçmemek.
- Şekil ve tablo adlarını son makale iskeletiyle eşleştirmek.

**Kaynak veri:** [MIT-BIH Noise Stress Test Database](https://physionet.org/content/nstdb/1.0.0/). Ham sinyal dosyaları bu depoda tutulmaz.
