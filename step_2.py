
out_f = open("temp_step_2.txt", "r")

print("Calculate number of string and number of letter in string")

i = 1
while True:
    my_str = out_f.readline()
    if len(my_str) == 0:
        break
    if '\n' in my_str:
        my_lenth = len(my_str) - 1
    else:
        my_lenth = len(my_str)
    print('in string number of', i, 'is', my_lenth, 'letter')
    i += 1
print('number of string=', i-1)

out_f.close()
