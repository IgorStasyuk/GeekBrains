import math


def my_generator(n):
    for i in range(1, n+1):
        el = math.factorial(i)
        yield el


print('Введите количество факториалов, которые надо вывести')

num = int(input())
gene = my_generator(num)

for i in range(0, num):
    print(next(gene))
