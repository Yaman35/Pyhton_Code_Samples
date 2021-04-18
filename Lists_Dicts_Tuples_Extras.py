# Örnek-1
list1 = [t for t in range (1, 14, 2)]  # 1'den 13'e kadar tek sayılı liste üretir.
print(list1)

list1[0], list1[-1] = list1[-1], list1 [0]  # Listenin ilk elemanı ile son elemanının yeri bu şekilde aynı anda değiştirilebilir.
print (list1)

# Örnek-2 
list2 = [i**2 for i in range (7,13)] # Liste içinde bu şekilde for,if döngüleri yazılabilir ve liste oluşturulabilir
print(list2)
list3 = [i**0.5 for i in list2 if i>81] # List2 elemanlarından 81 den büyü olanların karekökünü al demektir
print(list3)

# Örnek-3 
list4 = [10,10,20,20,20,30,30,30,30,40,60,80]
print (list4)
set_5 = {i/2 for i in list4} # Bu şekilde bir kullanım ile set lerde oluşturulabilir
print (set_5)

# Örnek-4
list6 = [i for i in range (10)] # Liste oluşturduk
dict1 = {x: x**2 for x in list6} # Bu şekilde bir kullanım ile dictionary lerde oluşturulabilir. list 6 elemanlarının kareleriyle birlikte
print (dict1)

# Örnek-5
list7 = ["Kahve","Meyve","Tatlı","Ana Yemek","Çorba"]
for i in reversed(list7): #reversed() fonksiyonu listeyi tersten yazar.
    print (i)

# Örnek-6
list8 = ["kara", "hava", "deniz"]
x = True if "hava" in list8 else False # Bu şekilde tek satırda da if else yapılabilmektedir.
print(x)

# Örnek-7
tuple1 = (1, 2, 3, 4, 5, 6, 789)
if 1 in tuple1:
    print ("Bu değer mevcut")

# Örnek-8
string1 = "veri bilimi, alanında, oldukça, fazla, kaynak, bulunur."
liste = string1.split(", ") # String1 cümlesinin kelimelerini ayrı ayrı birer eleman olacak şekilde liste yapar
print(liste)
x = "/".join(liste) # join() fonkiyonu içine aldığı iterable değişkenin elemanları arasına istenilen string ifadeyi koyar
print(x)

dict3={1:"masa", 2:"sandalye", 3:"bilgisayar"}
print ("+".join(dict3.values()))