list1=[t for t in range (1, 14, 2)]  # 1'den 13'e kadar tek sayılı liste üretir.
print (list1)
​
​
list1[0], list1[-1] = list1[-1], list1 [0]  #listenin ilk elemanı ile son elemanının yerini değiştirir.
print (list1)
​
## Örnek-2 ##
list2=[i**2 for i in range (7,13)]
print (list2)
list3=[i**0.5 for i in list2 if i>81]
print (list3)
## örnek-3 ##
list4=[10,10,20,20,20,30,30,30,30,40,60,80]
print (list4)
dict5={i/2 for i in list4}
print (dict5)
​
##  Örnek-4 ##
list6=[i for i in range (10)]
dict1={x: x**2 for x in list6}
print (dict1)
​
##  Örnek-5 ##
list7 = ["Kahve","Meyve","Tatlı","Ana Yemek","Çorba"]
for i in reversed(list7): #reversed fonksiyonu listeyi tersten yazar.
    print (i)
​
## Örnek-6 ##
list8= ["kara", "hava", "deniz"]
x=True if "hava" in list8 else False #Tek satırda if koşulu
print (x)
​
## Örnek-7##
tuple1=(1, 2, 3, 4, 5, 6, 789)
if 1 in tuple1:
    print ("Bu değer mevcut")
​
## Örnek-8 ##
string1="veri bilimi, alanında, oldukça, fazla, kaynak, bulunur."
print (string1.split(", "))
print ("-".join(string1))
​
dict3={1:"masa", 2:"sandalye", 3:"bilgisayar"}
print ("+".join(dict3.values()))