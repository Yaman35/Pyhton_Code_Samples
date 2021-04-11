# Girilen sayının rakamları toplamını veren kod

number = int(input("Enter a number: "))
toplam = 0
while number > 0:
  toplam += number % 10
  number = int(number/10)
print(toplam) 
