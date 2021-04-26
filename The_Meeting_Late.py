"""
Ornek : “Merhaba Kaya, toplantiya bugun 10 dk gec kaldiniz. Toplanti sonrasinda bana mazeretinizi lutfen e-mail ile iletiniz. Iyi calismalar.”

Gec kalan personel listesi:
 Isimler = [‘Kaya’, ‘Sinem’, ‘Peker’, ‘Jale’, ‘Fikret’, ‘Necmi’]
·     Gec kalma zamani, her personel toplantiya 10 dk gecikme artarak katiliyor.

Ornek: Kaya 10 dk gecikiyor, Sinem 20 dk, Peker 30dk, ….
Istenilen sonuc:
“Merhaba Kaya, toplantiya bugun 10 dk gec kaldiniz. Toplanti sonrasinda bana mazeretinizi lutfen e-mail ile iletiniz. Iyi calismalar.”
“Merhaba Sinem, toplantiya bugun 20 dk gec kaldiniz. Toplanti sonrasinda bana mazeretinizi lutfen e-mail ile iletiniz. Iyi calismalar.”
“Merhaba Peker, toplantiya bugun 30 dk gec kaldiniz. Toplanti sonrasinda bana mazeretinizi lutfen e-mail ile iletiniz. Iyi calismalar.”
“Merhaba Jale, toplantiya bugun 40 dk gec kaldiniz. Toplanti sonrasinda bana mazeretinizi lutfen e-mail ile iletiniz. Iyi calismalar.”
“Merhaba Fikret, toplantiya bugun 50 dk gec kaldiniz. Toplanti sonrasinda bana mazeretinizi lutfen e-mail ile iletiniz. Iyi calismalar.”
“Merhaba Necmi, toplantiya bugun 60 dk gec kaldiniz. Toplanti sonrasinda bana mazeretinizi lutfen e-mail ile iletiniz. Iyi calismalar.”
"""
# Çözüm - 1

isimler = ["Kaya", "Sinem", "Peker", "Jale", "Fikret", "Necmi"]
for i in range(len(isimler)):
    print(f"Merhaba {isimler[i]}, toplantiya bugun {(i+1)*10} dk gec kaldiniz. Toplanti sonrasinda bana mazeretinizi lutfen e-mail ile iletiniz. Iyi calismalar.")


# Çözüm - 2 

names = ["Kaya", "Sinem", "Peker", "Jale", "Fikret", "Necmi"]
arrive_times = [i*10 for i in range(1, len(names)+1)]
names_arrive_times = list(zip(names, arrive_times))
print(names_arrive_times)

for i in names_arrive_times:
    print(f"Merhaba{i[0]}, toplantiya bugun {i[1]} dk gec kaldiniz. Toplanti sonrasinda bana mazeretinizi lutfen e-mail ile iletiniz. Iyi calismalar")