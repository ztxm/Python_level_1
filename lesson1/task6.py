"""
6)	Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
 Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
 Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
 Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

result = float(input("Введите результат первого дня в км: "))
result_b = float(input("Введите целевой результат в км: "))
day = 1
result_next_day = result
while True:
    if result <= 0 or result_b <= 0:
        print(f"Результаты должны быть больше нуля")
        break
    if result_next_day > result_b:
        if day == 0:
            print(f"Спортсмен уже достигает результата")
            break
        print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {result_next_day:.0f} км.")
        break
    if day == 1:
        print(f"{day}-й день: {result_next_day}")
    result_next_day = result_next_day + (result_next_day * 0.1)
    day += 1
    print(f"{day}-й день: {result_next_day:.2f}")