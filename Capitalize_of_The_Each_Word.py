txt = "abckr trşuyışıçhl yşrpofok fçllgotıkf. dkefglşrşg"
txt1 = txt.split(" ") #split ile cümle içerisindeki kelimeleri boşluklardan olacak şekilde ayırıp her birini ayrı bir eleman olarak listeye atar
print(txt1)
print()
for i in txt1:
  print(i.capitalize() + " ", end=" ")

# Bilindiği üzere bu işlemi zaten title() methodu yapmaktadır

# Çözüm 2:

text = "the better the family, the better the society"
text = text.replace("t", "T", 8).replace("T", "t", 7).replace("t", "T", 5).\
replace("T", "t", 3).replace("t", "T", 1).replace("b", "B").replace("f", "F")\
.replace("s", "S")
print(text)
