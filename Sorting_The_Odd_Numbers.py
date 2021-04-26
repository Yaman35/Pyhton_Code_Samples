# Çözüm - 1

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
odd_list = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 1:
        odd_list.append(numbers[i])
        odd_list.sort()
        numbers[i] = "T"
counter = 0
for y in range(len(numbers)):
    if numbers[y] == "T":
        numbers[y] = odd_list[counter]
        counter += 1
print(numbers)

# Çözüm - 2

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
odd = []
numbers_n = []

for i in numbers:
    if i % 2 == 1:
        odd.append(i)
odd.sort(reverse=True)
print(odd)

for i in numbers:
    if i % 2 == 1:
        numbers_n.append(odd[-1])
        odd.pop()
    else:
        numbers_n.append(i)
print(numbers_n)
