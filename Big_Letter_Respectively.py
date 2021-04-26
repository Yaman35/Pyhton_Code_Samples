"""
Örnek olarak verilen stringin her bir karakteri sirasiyla buyuk harf haline gelecek ve sonuc bir liste seklinde olacak.

input = "iki kelime"
output = ['Iki kelime', 'iKi kelime', 'ikI kelime', 'iki Kelime', 'iki kElime', 'iki keLime', 'iki kelIme', 'iki keliMe', 'iki kelimE']
"""
sentence = input("Please enter a sentence : ")
liste = []

for i in range(len(sentence)):
    if sentence[i].isalpha():
        liste.append(sentence[:i] + sentence[i].upper() + sentence[i+1:])
print(liste)