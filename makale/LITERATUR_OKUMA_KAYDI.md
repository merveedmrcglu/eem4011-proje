# Yakın yayınlar: okuma ve erişim kaydı

Kontrol tarihi: 21 Kasım 2026. Bu kayıt, üç PDF'nin indirilip okunduğu anlamına gelmez.

| Kaynak | Erişim ve okuma durumu | Görev, veri, ölçüt | Bu projeye etkisi |
|---|---|---|---|
| [Rahman, Pal ve Karmakar (2025)](https://doi.org/10.1016/j.bspc.2025.108294) | [Kurumsal Figshare](https://figshare.com/articles/journal_contribution/Impact_and_mitigation_of_blind_filtering_in_automatic_ECG_analysis_for_wearable_sensors/29653379) üzerinden tam PDF indirildi; 9 sayfa, yöntem ve sınırlılıklar okundu. | Altı açık veri kümesinde gürültü algılama; veri kümesi dışarıda bırakmalı test. Gürültülü bölümü dışlama sonrasında aritmi sınıflandırma F1'i ve telefon/giyilebilir cihaz deneyi. Kendi sınırlılığı: gürültülü bölgeleri dışlamak veri kaybettirir; tek derivasyon. | Bizim R tepesi F1'imiz ile sınıflandırma F1'i doğrudan karşılaştırılamaz. Dış veri ve cihaz deneyi bizde yok. |
| [Sanz-Guerrero ve ark. (2026)](https://doi.org/10.1016/j.bspc.2026.109874) | Yayınevinin açık tam HTML metni okundu. PDF görüntüleyicide 13 sayfa açıldı, fakat dosya yerel olarak indirilemedi. | LUDB'de 200 kayıt, 12 derivasyon, kayıt düzeyinde eğitim/doğrulama/test; dikkat kapılı 1D U-Net ile P/QRS/T sınır ve tepeleri. ±150 ms ile R tepe F1'i de veriyor, ancak veri ve görev kapsamı farklı. | Bizim çalışmada öğrenilmiş yeni model, 12 derivasyon veya bağımsız kayıt testi yok. |
| [Costabile, Gualtieri ve Napoli (2026)](https://doi.org/10.1016/j.bspc.2026.109788) | Yayınevi özeti/ön izlemesi ve indekslenmiş HTML bölümleri okundu. Tam PDF yayınevi sayfasında kurum erişimi veya satın alma gerektiriyor; indirilmedi. | (1,4,1)/6 ağırlıklı üç örnekli PMA ön süzmesi; iki sentetik ve bir gerçek gürültülü EKG; MSE, SNR, PRD ile sinyal iyileştirme. | Bizim R tepesi F1 ölçütümüz ile bu sinyal onarma ölçütleri doğrudan kıyaslanamaz. |

## Sonuç

Tek cümlelik mevcut katkı, iki temel NSTDB kaydında sabit ön işleme yöntemlerini eşleştirilmiş pencerelerle karşılaştırır. Bu üç yayının yeni yöntem ve/veya daha geniş doğrulama düzeyine henüz ulaşmaz. Bağımsız kişi/kayıt testi yapılmadan genelleme veya klinik yarar iddiası kurulmaz.
