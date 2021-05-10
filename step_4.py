import random

final_list = []
print("Write number of elements =")
num = int(input())
my_list = [el for el in range(21)]
new_list = [random.choice(my_list) for k in range(num)]
print(my_list)
print(new_list)
for i in range(0, len(new_list)):
    if new_list.count(new_list[i]) == 1:
        final_list.append(new_list[i])

print(final_list)

