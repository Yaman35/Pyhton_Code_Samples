# Girilecek Sayı Listesindeki En Büyük İkinci Elemanı Bulma

scores = input("Scores: ").split(",")
scores2 = [int(scores[i]) for i in range(0, len(scores))]
scores2.sort()
print(scores2[-2])

scores = input("Please enter a score array: ").split()
arr = map(int, scores) # map() burada içine aldığı listenin her elemanını integer yapar, int yerine başka fonksiyon yazsaydık onu uygulardı
print (sorted(set(arr))[-2])
