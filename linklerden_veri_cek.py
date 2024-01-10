import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

# TXT dosyasındaki linkleri oku
with open('linklerson2.txt', 'r', encoding='utf-8') as file:
    links = file.read().splitlines()

# Excel dosyasını oluştur
df_all_comments = pd.DataFrame(columns=["Film Adı", "Konu"])

# Her bir link için işlem yap
for link in links:
    # Film adını ve sayfa adını çıkar
    film_name = link.split("/")[-1]

    # Web sayfasını çek
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Yorumları ve film türünü çek (Bu kısmı kendi sayfanıza göre uyarlayın)
    comments = soup.find_all(class_="text-collapsed")
    
    # Film Adı, Yorum ve Tür içeren DataFrame oluştur
    df_comments = pd.DataFrame({
        "Film Adı": [film_name] * len(comments),
        "Konu": [comment.text.strip() for comment in comments],
    })

    # DataFrame'leri birleştir
    df_all_comments = pd.concat([df_all_comments, df_comments], ignore_index=True)
    
# Excel'e yaz
df_all_comments.to_excel("film_yorumlari5.xlsx", index=False)

