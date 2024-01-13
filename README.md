# Film sitesinden aldığımız filmlerden verdiğimiz bir konuya göre en yakın filmi veren algoritma.

Bir benzerlik algoritmasıdır. Sinemalar sitesinden alınmış olan farklı türlerdeki filmler ile model eğitiliyor ve modele bir konu gönderildiğinde bunun hangi filme daha benzer olduğunu tespit ediyor.

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


### Konuların Temizlenmesi ve Lemmatization İşlemi<br/>
Veri setimizin başarı oranını yükseltmek için filmlerin konularını arındırmamız lazım. Konulardaki noktalama işaretleri, stopwordler vs. temizlememiz gerek. En son olarak lemmatization işlemi yapılarak kelimelerin köklerini alarak daha temiz ve modelin başarısını yükseltecek bir konu elde etmiş oluyoruz.

### Oluşturulan Temiz Konu Görseli

![WhatsApp Image 2024-01-10 at 21 58 41 (1)](https://github.com/Xpmian/Dogal-Dil-isleme-Projesi-/assets/115807439/07db955d-3338-4806-85c3-15b33da2148c)

<br/>

Veri seti'ndeki kolonlarımız aşağıdaki gibidir:<br/>
-Filmin İsmi<br/>
-Filmin Konusu<br/>
<br/>

# Modelin Oluşturulması ve Benzer Film Bulma<br/>

## Model Seçimi
Yapılacak işlemin hangi modelde daha yüksek başarı oranı vereceğini tespit etmek amacıyla araştırma yapılıp aynı zamanda bazı modeller üzerinde de test edilmiştir. Başlangıç olarak 3 popüler model üzerinde denemeler yapılmıştır. Bu modeller TD-IDF,Fuzzywuzzy ve Universal Sentence Encoder modelidir. Veri seti üzerinde bu modellerin aynı kelimelerdeki benzerlik oranı bulunmuştur. Projedeki test veri seti sonuçlarına bakıldığında:<br/>

Konu olarak "kaptan amerika" verdiğimizde 3 modelin önerdiği film ve benzerlik oranları:<br/><br/>
TD-IDF Modeli için  benzerlik: 0.4628 <br/> Önerilen Film: Kaptan Amerika 2<br/><br/>
![Screenshot_4](https://github.com/Xpmian/Dogal-Dil-isleme-Projesi-/assets/115807439/788f3f22-6981-4c94-b0cf-a5303fc7b695)
<br/>
<br>
Universal Sentence Encoder Modeli için benzerlik: 0.19874202 <br/> Önerilen Film: Guantanamo Yolu<br/>
![Screenshot_5](https://github.com/Xpmian/Dogal-Dil-isleme-Projesi-/assets/115807439/34c663bd-8aa5-49bf-b48a-2081b38385b8)

Fuzzywuzzy için benzerlik: %100 <br/>Önerilen Film: Yenilmezler<br/>
![Screenshot_6](https://github.com/Xpmian/Dogal-Dil-isleme-Projesi-/assets/115807439/843cbfdb-a992-411c-93c1-c72915db5a5c)

<br/>
Sonuçlar incelendiğinde Universal Sentence Encoder modelinin projede kullanılan veri setine göre önerdiği filmin çok başarısız olduğu görülmektedir. Diğer modeller için de Fuzzywuzzy modeli sadece kelime benzerliğine baktığı için iyi bir film ama çok yüksek ve güvenilir olmayan bir benzerlik oranı sunmuştur. Bu yüzden TD-IDF modeli kullanmak daha iyi olacaktır.<br>
<br>
<br>
<br>
Veri seti üzerinde bu modellerin aynı cümleler verilip benzerlik oranı bulunmuştur. Projedeki test veris eti sonuçlarına bakıldığında:<br/>
Konu olarak "Azılı suçlularla tıkabasa dolu bir hapishanenin yöneticileri, cezaevindeki mahkumları birbirleriyle dövüşmeye zorlar" verdiğimizde 3 modelin önerdiği film ve benzerlik oranları:<br/><br/>

TD-IDF Modeli için  benzerlik: 0.2665 <br/> Önerilen Film: Ölüm Yarışı<br/><br/>
![Screenshot_9](https://github.com/Xpmian/Dogal-Dil-isleme-Projesi-/assets/115807439/5c0fb140-9cf4-4059-8e68-a49bb9c40a2b)
<br/>
<br>
Universal Sentence Encoder Modeli için benzerlik: 0.6353595 <br/> Önerilen Film: Tut Sözünü<br/>
![Screenshot_8](https://github.com/Xpmian/Dogal-Dil-isleme-Projesi-/assets/115807439/a4549f76-e6c9-4ed3-bb92-19a475079277)

Fuzzywuzzy için benzerlik: %97 <br/>Önerilen Film: Ölüm Yarışı<br/>
![Screenshot_7](https://github.com/Xpmian/Dogal-Dil-isleme-Projesi-/assets/115807439/a6c5727b-8d7c-49ea-a4d3-fd310cb7047c)

Sonuçlar incelendiğinde Universal Sentence Encoder modelinin projede kullanılan veri setine göre önerdiği filmin çok başarısız olduğu görülmektedir. Diğer modeller için de Fuzzywuzzy modeli sadece kelime benzerliğine baktığı için iyi bir film ama çok yüksek ve güvenilir olmayan bir benzerlik oranı sunmuştur. Bu yüzden TD-IDF modeli kullanmak daha iyi olacaktır.<br>
<br>
<br>
TD-IDF modeli kelime frekanslarına dayalı bir yaklaşım kullanırken Universal Sentence Encoder modeli daha geniş bir metin anlama yeteneğine sahiptir.
<br>
<br>
Fuzzywuzzy kütüphanesi ise metin benzerliğini değerlendirmek için farklı bir yöntem kullanır. Bu yöntem karakter dizileri arasındaki benzerliği ölçer.
<br>
<br>
TD-IDF kelime frekanslarını temel alan bir vektörleme yöntemidir. Kısa metinlerde veya benzer anlam taşıyan ifadelerde sınırlı bir anlama sahip olabilir.
<br>
<br>
Universal Sentence Encoder geniş bir metin anlama yeteneğine sahiptir ve kısa metinlerle başa çıkabilir.
<br>
<br>
Fuzzywuzzy kütüphanesi, karakter dizileri arasındaki benzerliği değerlendirir ve metinler arasında benzerlik bulma konusunda oldukça hassastır. Ancak, anlamın derinlemesine anlaşılması konusunda sınırlıdır.
<br>
