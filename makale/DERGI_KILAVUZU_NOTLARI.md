# BSPC yazar kılavuzu kontrolü (21 Kasım 2026)

Kaynak: [Biomedical Signal Processing and Control — Guide for Authors](https://www.sciencedirect.com/journal/biomedical-signal-processing-and-control/publish/guide-for-authors). Bu notlar başvuru yapıldığı anlamına gelmez.

| Konu | Resmî kılavuzdaki koşul | Bu taslakta durum |
|---|---|---|
| Makale türü ve uzunluk | Full paper normalde yaklaşık 5.000 kelime; short communication tipik 2.000; Technical Note yaklaşık 5.000 kelime ve en çok 5 görsel. | Tür henüz kesinleşmedi; mevcut 3 sayfalık iskelet tam makale değil. |
| Özet ve anahtar kelime | Özet en çok 250 kelime; İngilizce 1–7 anahtar kelime. | Geçici özet sınır içinde; beş anahtar kelime var. |
| Highlights | Ayrı düzenlenebilir dosyada zorunlu; 3–5 madde, her madde boşluklar dahil en çok 85 karakter. | Dört maddelik `makale/highlights.txt` hazır. |
| Graphical abstract | Teşvik ediliyor; zorunlu değil; ayrı dosya. | Hazırlanmadı. |
| Hakemlik | Single-anonymized; uygun bulunan çalışmalar genellikle en az iki hakeme gönderilir. | Bilgi amaçlı. |
| LaTeX ve dosya | Kaynak `.tex` olmalı, PDF kaynak dosya olarak kabul edilmez. Kılavuz belirli LaTeX sınıfı adı vermiyor. | İskelette `elsarticle` kullanılıyor. |
| Şekiller | Metinde atıf, sırayla numara, açıklama ve her şekil için ayrı dosya. Okunabilir çözünürlük istenir. | F1 grafiği iskelette atıf ve açıklamayla eklendi; ayrıca ayrı PNG dosyası var. |
| Kaynaklar | Metindeki her atıf listede ve listedeki her kaynak metinde olmalı. Köşeli parantez içinde geçiş sırasına göre numara; DOI varsa eklenir. | Mevcut iskelette atıflar ve kaynakça eşleşiyor. İki ek PDF yalnız okuma kaydında; makale metninde kullanılmadı. |
| Veri | Bu dergide Option C: araştırma verisini uygun depoya koyup bağlantı vermek veya paylaşamama gerekçesini yazmak zorunlu. | Ham NSTDB verisine kaynak bağlantısı var; türetilmiş sonuçların paylaşımı ayrıca düzenlenecek. |
| Çıkar çatışması ve destek | Çıkar çatışması beyanı ve finansman kaynağı bilgisi istenir. | Öğrencinin doğrulayacağı gerçek durum yazılmalı; varsayım yapılmaz. |
| Yazar katkısı | CRediT rolleri istenir. | Son yazarlık ve roller doğrulanmalı. |
| Yapay zekâ | Metin hazırlığında kullanıldıysa kaynakçadan **önce** `Declaration of generative AI and AI-assisted technologies in the manuscript preparation process` başlığıyla beyan edilir. Yazar metni denetler ve sorumluluğu üstlenir; AI yazar olamaz. Veri temelli grafikler gerçek veriden tekrarlanabilir hesapla oluşturulabilir; gözlenen/deneysel birincil veri görüntüsü AI ile uydurulamaz veya değiştirilemez. | Taslakta beyan başlığı var; son metin kullanıcı tarafından kontrol edilmeli. |
| Açık erişim ücreti | Abonelik ve açık erişim seçenekleri var; kılavuz sayfasında belirli APC tutarı yok. | Ücret tahmin edilmedi. |

## Bu proje için sonuç

Kapsam, derginin EKG işleme ve gürültüye dayanıklılık alanıyla örtüşüyor. Buna rağmen mevcut iki temel kayıt üzerindeki sabit yöntem karşılaştırması, bir full paper için yeterli özgün katkı ve bağımsız doğrulama göstermez. Üç yakın yayının veri, yöntem ve metrikleri farklıdır; F1 sayıları arasında doğrudan üstünlük iddiası kurulmaz. Önce bağımsız kayıtlar üzerinde önceden belirlenmiş değerlendirme ve literatür karşılaştırması gerekir.
