

def my_func(str, arg1):
    mybool = True
    my_list = str.split()
    my_sum = 0
    for i in range(0, len(my_list)):

        my_sum = my_sum + int(my_list[i])
        if my_list[i] == 'q':
            mybool = Faulse
    return my_sum, mybool


print ('Введите числа разделенные пробелом, чтобы остановить программу введите q')
str = input()
num1 = 0
my_num = 0
my_bool = True

while my_bool == True:
    num1, my_bool = my_func(str, num1)
    my_num = my_num + num1
    print(my_num)
    str = input()

print('конец')

