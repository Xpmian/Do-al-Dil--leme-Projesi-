# Film sitesinden aldığımız filmlerden verdiğimiz bir konuya göre en yakın filmi veren algoritma.

Bir sınıflandırma algoritmasıdır. Twitterdan alınmış olan farklı kategorilerdeki (Siyaset, Ekonomi, Spor, Teknoloji ve Bilim) tweetleri ile model eğitiliyor ve modele bir tweet gönderildiğinde bunun hangi kategoride bir tweet olduğunu tespit ediyor.

Kullanılan Kütüphaneler<br/>

-Pandas<br/>
-NumPy<br/>
-Selenium<br/>
-spaCy<br/>
-Nltk<br/>
-Scikit-learn<br/>




# VERİ SETİ'NİN OLUŞTURULMASI

Veri setimiz film adlarından ve filmlerin konularından oluşuyor. Verisetimiz oluşturmak için www.sinemalar.com sitesini seçtik.

Öncelikle selenium kütüphanesini kullanarak sitenin tüm filmleri sayfa sayfa gösterdiği https://www.sinemalar.com/filmler adresinden tüm filmlerin kendi sayfalarının linklerini bir txt dosyası olarak kaydettik. 

![WhatsApp Image 2024-01-10 at 21 58 41](https://github.com/Xpmian/Dogal-Dil-isleme-Projesi-/assets/115807439/dcd3cf16-0dc1-4f73-900c-9aba02c47ece)


Ardından aldığımız linkleri teker teker gezdik ve filmin sayfasından adını ve konusunu aldık.

![WhatsApp Image 2024-01-10 at 21 58 40](https://github.com/Xpmian/Dogal-Dil-isleme-Projesi-/assets/115807439/b243f4d1-1f4a-40b3-83d5-064b9885a1a2)


Tweetlerin Temizlenmesi ve Lemmatization İşlemi
Veri setimizin başarı oranını yükseltmek için filmlerin konularını arındırmamız lazım. Konulardaki noktalama işaretleri, stopwordler vs. temizlememiz gerek. En son olarak lemmatization işlemi yapılarak kelimelerin köklerini alarak daha temiz ve modelin başarısını yükseltecek bir konu elde etmiş oluyoruz.

## Oluşturulan Temiz Tweet Görseli

![WhatsApp Image 2024-01-10 at 21 58 41 (1)](https://github.com/Xpmian/Dogal-Dil-isleme-Projesi-/assets/115807439/07db955d-3338-4806-85c3-15b33da2148c)

<br/>

Veri seti'ndeki kolonlarımız aşağıdaki gibidir:<br/>
-Filmin İsmi<br/>
-Filmin Konusu<br/>
<br/>

# Modelin Oluşturulması ve Benzer Film Bulma<br/>

## Model Seçimi
Yapılacak işlemin hangi modelde daha yüksek başarı oranı vereceğini tespit etmek amacıyla araştırma yapılıp aynı zamanda bazı modeller üzerinde de test edilmiştir. Başlangıç olarak 3 popüler model üzerinde denemeler yapılmıştır. Bu modeller TD-IDF,Fuzzywuzzy ve Universal Sentence Encoder modelidir. Veriseti üzerinde bu modellerin aynı kelimelerdeki benzerlik oranı bulunmuştur. Projedeki test veriseti sonuçlarına bakıldığında:<br/>

Konu olarak "kaptan amerika" verdiğimizde 3 modelin önerdiği film ve benzerlik oranları:<br/><br/>
TD-IDF Modeli için  benzerlik: 0.4628 <br/> Önerilen Film: Kaptan Amerika 2<br/><br/><br/>
Universal Sentence Encoder Modeli için benzerlik: 0.19874202 <br/> Önerilen Film: Guantanamo Yolu<br/><br/><br/>
Fuzzywuzzy için benzerlik: %100 <br/>Önerilen Film: Yenilmezler<br/>
<br/>
Sonuçlar incelendiğinde Universal Sentence Encoder modelinin projede kullanılan verisetine göre önerdiği filmin çok başarısız olduğu görülmektedir. Diğer modeller için de Fuzzywuzzy modeli sadece kelime benzerliğine baktığı için iyi bir film ama çok yüksek ve güvenilir olmayan bir benzerlik oranı sunmuştur. Bu yüzden TD-IDF modeli kullanmak daha iyi olacaktır.
