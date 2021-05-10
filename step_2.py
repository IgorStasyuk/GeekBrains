import random

my_list = []
new_list = []
print("Write number of elements =")
num = int(input())
my_list = [el for el in range(0, num)]
random.shuffle(my_list)
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        new_list.append(my_list[i])

print(my_list)
print(new_list)
