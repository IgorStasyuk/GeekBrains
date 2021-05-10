

def my_func1(x, y):
    n = x ** y
    return n

def my_func2(x, y):
    n = 1
    while y < 0:
        n = n / x
        y += 1
    return n


print ('Программа возведения чисел в степень')
print ('Введите действительное положительное число')
num1 = float(input())
print ('Введите целое отрицательное число')
num2 = int(input())
print (my_func1(num1, num2))
print (my_func2(num1, num2))
