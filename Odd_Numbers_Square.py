# Verilen bir listedeki tek sayıların karesini alma

my_list = [1, 2, 3, 4, 5, 6]
new_list = []

for x in my_list:
  if x % 2 != 0:
    new_list.append(pow(x,2))

print(new_list)

# [expression for item in list execution body if condition]

my_list = [1, 2, 3, 4, 5, 6]
print([x ** 2 for x in my_list if x % 2 != 0]) 
