out_f = open("temp_step_6.txt", "r")
my_dict = dict()
my_second_item = []
my_one_item = []

while True:
    my_temp_str = out_f.readline()
    if my_temp_str == "":
        break
    my_str = my_temp_str.split()
    my_one_item.append(my_temp_str.split(":")[0])
    num = 0
    for i in range(1, len(my_str)):
        n = 0
        temp = 0
        for k in range(0, len(my_str[i])):

            if my_str[i][k].isdigit():
                n += 1

        if n != 0:
            temp = int(my_str[i][:n])
        else:
            temp = 0
        num += temp
    my_second_item.append(num)

my_dict = dict(zip(my_one_item, my_second_item))



print(my_dict)
print(my_one_item)
print(my_second_item)


out_f.close()
