Film sitesinden aldığımız filmlerden verdiğimiz bir konuya göre en yakın 5 filmi veren algoritma.

Bir sınıflandırma algoritmasıdır. Twitterdan alınmış olan farklı kategorilerdeki (Siyaset, Ekonomi, Spor, Teknoloji ve Bilim) tweetleri ile model eğitiliyor ve modele bir tweet gönderildiğinde bunun hangi kategoride bir tweet olduğunu tespit ediyor.

Kullanılan Kütüphaneler
-Pandas
-NumPy
-Selenium
-spaCy
-Nltk
-Scikit-learn

VERİ SETİ'NİN OLUŞTURULMASI

Veri setimiz film adlarından ve filmlerin konularından oluşuyor. Verisetimiz oluşturmak için www.sinemalar.com sitesini seçtik.

Öncelikle selenium kütüphanesini kullanarak sitenin tüm filmleri sayfa sayfa gösterdiği https://www.sinemalar.com/filmler adresinden tüm filmlerin kendi sayfalarının linklerini bir txt dosyası olarak kaydettik. 

[Uploading WhatsApp Image 2024-01-10 at 21.58.41.jpeg…]()


Ardından aldığımız linkleri teker teker gezdik ve filmin sayfasından adını ve konusunu aldık.

[film konuları ve uzunluğu]


Tweetlerin Temizlenmesi ve Lemmatization İşlemi
Veri setimizin başarı oranını yükseltmek için filmlerin konularını arındırmamız lazım. Konulardaki noktalama işaretleri, stopwordler vs. temzilememiz gerek. En son olarak lemmatization işlemi yapılarak kelimelerin köklerini alarak daha temiz ve modelin başarısını yükseltecek bir konu elde etmiş oluyoruz.


Veriseti oluşturulduktan sonra modelin daha iyi çalışması ve başarı oranının daha yüksek olması için tweetlerin temizlenmesi gerekmektedir. Tweetlerin içerisinde emojiler, noktalama işaretleri, stopwordsler, linkler gibi istenmeyen ve modelin başarısını düşürecek veriler tweetlerin içerisinden temizleniyor. Daha sonra lemmatization (kelimelerin köklerinin alınması) işlemi yapılarak temiz ve kelimelerin köklerinden oluşan tweetler elde ediliyor.


Oluşturulan Temiz Tweet Görseli

[cleankonu
