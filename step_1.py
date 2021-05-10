from sys import argv

script_name, time_of_work, cash_in_hour, prize = argv

print("Имя скрипта: ", script_name)
print("Время работы=", time_of_work)
print("Оплата в час=", cash_in_hour)
print ("Премия=", prize)

print(int(time_of_work) * int(cash_in_hour) + int(prize))