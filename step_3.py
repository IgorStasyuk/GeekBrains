
out_f = open("temp_step_3.txt", "r")
my_key_str = []
my_velue_str = []
workes_20 = {}
i = 1
while True:
    if i % 2 != 0:
        temp = out_f.readline()
        if temp == '':
            break
        if '\n' in temp:
            my_key_str.append(temp[:-1])
        else:
            my_key_str.append(temp)

    else:
        temp = out_f.readline()
        if temp == '':
            break
        if '\n' in temp:
            my_velue_str.append(int(temp[:-1]))
        else:
            my_velue_str.append(int(temp))
    i += 1
workes = dict(zip(my_key_str, my_velue_str))
print(workes)
money = 0
for salary in my_velue_str:
    money = money + salary

for i in my_key_str:
    if workes.get(i) <= 20000:
        workes_20[i] = workes.get(i)


print('Средний доход=', money/len(workes))
print('работники с зарплатой меньше 20000')
print(workes_20.keys())

out_f.close()
