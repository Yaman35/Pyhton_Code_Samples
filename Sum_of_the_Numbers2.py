# Girilen sayıya kadar olan (girilen sayı dahil) sayıları toplama

num = int(input("Please enter a number = "))
liste = []
for i in range(1,num+1):
    liste.append(i)
print(sum(liste)) 
