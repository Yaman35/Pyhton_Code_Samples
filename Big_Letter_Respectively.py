"""
Örnek olarak verilen stringin her bir karakteri sirasiyla buyuk harf haline gelecek ve sonuc bir liste seklinde olacak.

input = "iki kelime"
output = ['Iki kelime', 'iKi kelime', 'ikI kelime', 'iki Kelime', 'iki kElime', 'iki keLime', 'iki kelIme', 'iki keliMe', 'iki kelimE']
"""

# Çözüm -1

sentence = input("Please enter a sentence : ")
liste = []

for i in range(len(sentence)):
    if sentence[i].isalpha():
        liste.append(sentence[:i] + sentence[i].upper() + sentence[i+1:])
print(liste)



# Çözüm - 2

test = "iki kelime"
liste = []

for i, x in enumerate(test):
    if x != ' ':
        x = x.upper()
        for y in test[i]:
            y = x
            changed_test_1 = test[i:].replace(test[i], y, 1)
            changed_test = test[:i] + changed_test_1
            liste.append(changed_test)
print(liste)


# Çözüm - 3 

test = "algoritma öğrenmek lazım"
list_first = list(test)
list_second = []

for i in range (0, len(list_first)-1):
    if list_first[i].isalpha():       # isalpha() methodu ile listelenen elamanın harf olup olmadığı kontrol edilir
        list_first[i] = list_first[i].upper()
        converted = "".join(list_first) # join() methodu ile yaptığımız listeyi geri aldık, test haline geri çeviriyoruz
        list_second.append(converted)  # Tek harfi büyük olan test versiyonunu boş olan list_second a atıyoruz
        list_first = list(test)     # list_first ü tekrar eski ilk haline çeviriyoruz ki , sadece istediğimiz harf büyük olsun

print(list_second)