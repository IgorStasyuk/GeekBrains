from itertools import cycle

my_list = [el for el in range(6)]
print('Сколько раз вывести значения?')
num = int(input())
k = 0
for el in cycle(my_list):
    if k > num:
        break
    print(el)
    k += 1
