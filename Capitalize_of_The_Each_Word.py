txt = "abckr trşuyışıçhl yşrpofok fçllgotıkf. dkefglşrşg"
txt1 = txt.split(" ") #split ile cümle içerisindeki kelimeleri boşluklardan olacak şekilde ayırıp her birini ayrı bir eleman olarak listeye atar
print(txt1)
print()
for i in txt1:
  print(i.capitalize() + " ", end=" ")

# Bilindiği üzere bu işlemi zaten title() methodu yapmaktadır