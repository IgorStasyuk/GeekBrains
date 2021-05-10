def delenie(arg1, arg2):
    itog = arg1 / arg2
    return itog


print ('Введите 2 числа')
num1 = int(input())
num2 = int(input())
while num2 == 0:
    print('введите второе число не равное 0')
    num2 = int(input())
print (delenie(num1, num2))
