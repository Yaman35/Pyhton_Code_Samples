# Girilen sayının rakamları toplamını veren program

a = int(input("Rakam giriniz:  "))
l = 0
while a > 0:
  l += a % 10
  a = int(a/10)
print(l)