# Girilen Sayının Rakamları Toplamını Bulma 

# Çözüm - 1

number = int(input("Enter a number: "))
toplam = 0
while number > 0:
  toplam += number % 10
  number = int(number/10)
print(toplam)  

# Çözüm - 2 

rakamlar = []
for i in input("rakamları toplamını bulmak için bir sayı giriniz"):
    rakamlar.append(int(i))
print(sum(rakamlar))

# Çözüm - 3

sayi = int(input("Enter a number: "))
top = 0
for i in str(sayi):
  top += int(i)
print(top)

# Çözüm - 4

top=0
for i in input("sayı giriniz"):
  top += int(i)
print(top) 
