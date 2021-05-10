
my_middle = 0
k = 0
my_dict = {}
final_list = []
my_list_firm = []
my_firm_cash = []
with open("temp_step_7.txt") as f_obj:
    while True:
        my_str = f_obj.readline()
        if my_str == "":
            break
        my_temp_str = my_str.split()
        my_list_firm.append(my_temp_str[0])
        my_firm_cash.append(float(my_temp_str[2]) - float(my_temp_str[3]))
my_dict = dict(zip(my_list_firm, my_firm_cash))

for i in range(0, len(my_firm_cash)):
    temp_cash = my_firm_cash[i]
    if temp_cash <= 0:
        k += 1
        temp_cash = 0

    my_middle += temp_cash
my_average_profit = dict(average_profit=my_middle/(len(my_firm_cash) - k))
final_list = list[my_dict, my_average_profit]
print(my_dict)
print('средняя прибыль:', my_middle/(len(my_firm_cash) - k))
print(final_list)
