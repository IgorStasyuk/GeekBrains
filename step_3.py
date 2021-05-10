def my_func(arg1, arg2, arg3):
    num = min(arg1, arg2, arg3)
    summ = arg1 + arg2 + arg3 - num
    return summ
print('Введите 3 числа и получите сумму двух максимальных')
num1 = int(input())
num2 = int(input())
num3 = int(input())

print(my_func(num1, num2, num3))
