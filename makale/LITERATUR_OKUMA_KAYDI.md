# Yakın yayınlar: okuma ve erişim kaydı

Kontrol tarihi: 21 Kasım 2026. Aşağıdaki üç yakın çalışmadan yalnız Rahman'ın tam PDF'i indirildi. Sanz-Guerrero tam HTML üzerinden okundu; Costabile için yalnız erişilebilir ön izleme incelendi.

| Kaynak | Erişim ve okuma durumu | Görev, veri, ölçüt | Bu projeye etkisi |
|---|---|---|---|
| [Rahman, Pal ve Karmakar (2025)](https://doi.org/10.1016/j.bspc.2025.108294) | [Kurumsal Figshare](https://figshare.com/articles/journal_contribution/Impact_and_mitigation_of_blind_filtering_in_automatic_ECG_analysis_for_wearable_sensors/29653379) üzerinden tam PDF indirildi; 9 sayfa, yöntem ve sınırlılıklar okundu. | Altı açık veri kümesinde gürültü algılama; veri kümesi dışarıda bırakmalı test. Gürültülü bölümü dışlama sonrasında aritmi sınıflandırma F1'i ve telefon/giyilebilir cihaz deneyi. Kendi sınırlılığı: gürültülü bölgeleri dışlamak veri kaybettirir; tek derivasyon. | Bizim R tepesi F1'imiz ile sınıflandırma F1'i doğrudan karşılaştırılamaz. Dış veri ve cihaz deneyi bizde yok. |
| [Sanz-Guerrero ve ark. (2026)](https://doi.org/10.1016/j.bspc.2026.109874) | Yayınevinin açık tam HTML metni okundu. PDF görüntüleyicide 13 sayfa açıldı, fakat dosya yerel olarak indirilemedi. | LUDB'de 200 kayıt, 12 derivasyon, kayıt düzeyinde eğitim/doğrulama/test; dikkat kapılı 1D U-Net ile P/QRS/T sınır ve tepeleri. ±150 ms ile R tepe F1'i de veriyor, ancak veri ve görev kapsamı farklı. | Bizim çalışmada öğrenilmiş yeni model, 12 derivasyon veya bağımsız kayıt testi yok. |
| [Costabile, Gualtieri ve Napoli (2026)](https://doi.org/10.1016/j.bspc.2026.109788) | Yayınevi özeti/ön izlemesi ve indekslenmiş HTML bölümleri okundu. Tam PDF yayınevi sayfasında kurum erişimi veya satın alma gerektiriyor; indirilmedi. | (1,4,1)/6 ağırlıklı üç örnekli PMA ön süzmesi; iki sentetik ve bir gerçek gürültülü EKG; MSE, SNR, PRD ile sinyal iyileştirme. | Bizim R tepesi F1 ölçütümüz ile bu sinyal onarma ölçütleri doğrudan kıyaslanamaz. |

## PDF'i indirilen iki ek BSPC çalışması

Bu çalışmalar derginin güncel EKG makalelerini ve katkı düzeyini anlamak için eklendi. Her ikisinin de erişilen sürümü yayınevinin son PDF'i değil, yazar ön baskısıdır. Bu nedenle aşağıdaki açıklamalar okunan ön baskı sürümüne dayanır; yayımlanmış sürümdeki sayılarla eşdeğer kabul edilmez. PDF'ler telif ve sürüm karışıklığı yaratmamak için GitHub'a yüklenmedi; yerel `output/makale_kaynaklari` klasöründe tutulur.

| Çalışma ve PDF | Okunan yöntem/sonuç/sınırlılık | Bizim projeyle ilişki |
|---|---|---|
| [Lence ve ark., ECGtizer, DOI: 10.1016/j.bspc.2025.108710](https://doi.org/10.1016/j.bspc.2025.108710); [arXiv ön baskısı](https://arxiv.org/abs/2412.12139), yerel `ECGtizer_2025.pdf` (37 sayfa) | Kâğıt EKG görüntüsünden derivasyonları bulma, piksel tabanlı sinyal çıkarma ve eksik kısımları öğrenilmiş modelle tamamlama. JOCOVID ve PTB-XL üzerinde başka sayısallaştırma araçlarıyla karşılaştırma. Ön baskının sınırlılığı: temiz, dijital olarak oluşturulmuş kâğıt benzeri EKG'lere yoğunlaşan testler; gerçek kâğıt üzerindeki kırışık, not ve tarama kalitesi değişimi için daha fazla doğrulama gerekiyor. | Bizim veri doğrudan dijital NSTDB sinyalidir; kâğıttan sayısallaştırma veya 12 derivasyon rekonstrüksiyonu yapmıyoruz. R tepesi F1'i bu çalışmanın sayısallaştırma ölçüleriyle karşılaştırılamaz. |
| [Rebollo-Neira ve ark., kalp atımı morfolojisi, DOI: 10.1016/j.bspc.2025.107703](https://doi.org/10.1016/j.bspc.2025.107703); [arXiv ön baskısı](https://arxiv.org/abs/2301.06538), yerel `RebolloNeira_2025_preprint.pdf` (17 sayfa) | Sözlük öğrenmesi ve seyrek temsil ile MIT-BIH Arrhythmia veri setinde normal/ventriküler atım sınıflandırması; kişi içi ve kişiler arası değerlendirme ayrı. **Ön baskıdaki** kişiler arası başarı, kişi içi başarıdan düşük. Yayımlanmış sürümdeki sayılar farklı olabilir; buraya sayısal üstünlük aktarılmadı. | Bu çalışma R tepesi yerini değil, çıkarılmış atımın sınıfını tahmin ediyor. Kişiler arası test tasarımı bizim iki temel kayıtla sınırlı değerlendirmemizde eksik. |

**PDF sayımı:** Rahman'ın makale PDF'i ile bu iki yazar ön baskısı olmak üzere üç tam metin PDF yerel olarak mevcut ve yöntem/sonuç/sınırlılıkları incelendi. Buna karşılık başlangıçta seçilen **üç yakın makalenin** üç PDF'i mevcut değildir. Bu iki ifade birbirinin yerine kullanılmamalıdır.

## Sonuç

Tek cümlelik mevcut katkı, iki temel NSTDB kaydında sabit ön işleme yöntemlerini eşleştirilmiş pencerelerle karşılaştırır. Bu üç yayının yeni yöntem ve/veya daha geniş doğrulama düzeyine henüz ulaşmaz. Bağımsız kişi/kayıt testi yapılmadan genelleme veya klinik yarar iddiası kurulmaz.
