hafta_ucret = 200 # haftalık ücreti 200 dolar
hafta_saat= int(input("Mary hanım bu hafta kaç saat çalıştı?= ")) # Mary hanım bu hafta kaç saat çalıştı giriniz.

def maas_hesapla():

    if hafta_saat < 40: # eğer bu hafta izin kullanıp 40 saatten az çalıştıysa saat başı 50 dolar eksik alır.
        print((hafta_ucret-50)*hafta_saat)
    elif hafta_saat == 40: # eğer bu hafta 40 saat çalıştıysa normal haftalık ücreti alır.
        print(hafta_ucret*hafta_saat)
    else:  # eğer 40 saatten fazla çalıştıysa, çalıştığı 40 saat sonrası için saat başı 15 dolar fazla alır.
        salary = 40*200
        for i in range(hafta_saat-40): 
            salary += 15
        print(salary)

maas_hesapla() # En son tanımladığımız fonksiyonu çağırmamız gerek