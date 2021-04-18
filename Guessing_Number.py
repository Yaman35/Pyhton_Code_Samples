# Sayı Tahmin Etme Oyunu

import random
number = random.randint(1,101) # random sınıfının randint() fonksiyonu çağırılmıştır
attempt = 0

while True:
  answer = int(input("Take a guess 1-100: "))
  if answer < number:
    print("Increase!")
    attempt += 1        # Burada attempt değikenini her defasında 1 arttırarak klllanıcının kaç seferde tahmin ettiğini çıktı olarak alabiliriz.
  elif answer>number :
    print("Decrease")
    attempt += 1
  elif answer == number :
    print("Yes!")
    break
print(f"You've found in {attempt} times")
