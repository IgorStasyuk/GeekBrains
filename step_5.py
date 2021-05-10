out_f = open("temp_step_5.txt", "r")
my_str = out_f.readline().split()
temp = 0
for i in range(0, len(my_str)):
    num = int(my_str[i])
    temp = temp + num

print(my_str)
print(temp)

out_f.close()
