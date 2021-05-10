
out_f = open("temp_step_1.txt", "w")

print("Write your string")
my_str = input()

while my_str != '':
    out_f.writelines(my_str + '\n')
    my_str = input()

out_f.close()
print("end")
