# Eğer elimizde bir text var ve biz bu textin içindeki anagramların listesini istiyorsak
def anagram(text):
  liste=[x.strip(".<,*=)(/+&?£_|:;~!\$}]>[{#").lower() for x in text.split()]
  sorted_list=[]
  group_list=[]
  anagrams=[]
  for i in liste:
    if sorted(i) not in sorted_list:
      sorted_list.append(sorted(i))
  for a in range(len(sorted_list)):
    group_list.append([i for i in liste if sorted(i)==sorted_list[a]])
  for i in group_list:
    if len(i)>=2:
      anagrams.append(i)
  return anagrams
print(anagram("listen silent ROOPA TABU. OOPAR BUAT PAROO Soudipta? Kheyali Park Tollygaunge BUTA AROOP* Love AOORP +Protijayi Paikpara dipSouta/ Shyambazaar jayiProti North Calcutta Sovabazaar"))

