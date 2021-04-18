repeat = int(input("How many number will you enter?: "))
list_1 = []
for i in range(1,repeat+1):
    number = input(f"Please enter the {i}. number: ")
    list_1.append(number)
print(list_1)
list_1.sort()
print(f"The largest number is: {list_1[-1]}")
