"""
3)	Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

a = int(input("Введите целое число от 1 до 12: "))
month_list = ["зима", "весна", "лето", "осень"]
month_dict = {1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12: 3}

if 0 < a < 3 or a == 12: print(month_list[0])
elif 2 < a < 6: print(month_list[1])
elif 5 < a < 9: print(month_list[2])
elif 8 < a < 12: print(month_list[3])
else:
    print("Ошибка")

if 0 < a < 13:
    print(f"Через dict: {month_list[month_dict.pop(a)]}")
else:
    print("Ошибка")




