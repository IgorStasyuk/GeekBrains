from itertools import count


my_list = [el for el in range(101)]
print('Введите начальное значение и шаг с которым выводить список')
num = int(input())
step = int(input())

for el in count(num, step):
    if el > 101:
        break
    else:
        print(el)
