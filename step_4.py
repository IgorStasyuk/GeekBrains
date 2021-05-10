
my_dict = dict(One='Один', Two= 'Два', Three= 'Три', Four= 'Четыре')
out_f = open("temp_step_4.txt", "r")
new_list_str = []
while True:
    my_str = out_f.readline()
    if my_str == '':
        break
    temp_str = my_str.split()
    if temp_str[0] in my_dict.keys():
        temp_str[0] = my_dict.get(temp_str[0])
        new_str = ' '.join(temp_str)
        new_list_str.append(new_str)


print(*new_list_str, sep="\n", end="\n\n")
in_f = open("new_temp_step_4.txt", "w")
for i in range(0, len(new_list_str)):
    in_f.write(new_list_str[i] + "\n")

out_f.close()
in_f.close()
