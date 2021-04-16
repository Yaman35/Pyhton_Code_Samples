from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

def speak(string):
    tts=gTTS(text=string, lang="tr")
    file="answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

import random


def sans_oyunu():
    speak("Şans topu oyununa hoşgeldiniz...")
    kac_kez=int(input("kaç kez oynamak istersiniz= "))
    speak(str(kac_kez)+"kez oynamak isterim...")
    puan=kac_kez*10
    speak(str(puan)+"puanla oyuna başlıyorsunuz...")
    hak=0
    for i in range(0,kac_kez):
        hak=hak+1
        sayi=int(input("Lütfen sayıyı giriniz= "))
        speak(str(sayi)+" sayısını değer olarak girdiniz")
        sayi_tahmin=random.randint(1,100)
        if sayi>sayi_tahmin:
            puan=puan-10
            speak("Lütfen daha küçük bir sayı giriniz.")
            speak("Sizin girdiğiniz sayı"+str(sayi))
            speak("Tahmin edilen sayı"+str(sayi_tahmin))
            speak("Puanınız"+str(puan))
        elif sayi<sayi_tahmin:
            puan=puan-10
            speak("Lütfen daha Büyük bir sayı giriniz.")
            speak("Sizin girdiğiniz sayı"+str(sayi))
            speak("Tahmin edilen sayı"+str(sayi_tahmin))
            speak("Puanınız"+str(puan))
        elif sayi==sayi_tahmin:
            puan=puan+10
            speak("Tebrikler doğru tahminde bulundunuz..")
            speak("Sizin girdiğiniz sayı"+str(sayi))
            speak("Tahmin edilen sayı"+str(sayi_tahmin))
            speak("Puanınız"+str(puan))
            
        if hak==kac_kez:
            speak("Hakkınız sona erdi")
            speak("Puanınız"+str(puan))