"""
2)	Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
 город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
"""

def my_func(name, lastname, year, city, email, tel):
    print(f"Имя - {name} \n"
          f"Фамилия - {lastname} \n"
          f"Год рождения - {year}\n"
          f"город проживания - {city} \n"
          f"email - {email}\n"
          f"телефон - {tel}")

my_func(name="Вадим", lastname="Кузнецов", year="1987", city="Мск", email="mail@gmail.com", tel="+7 923 123 1234")

#ещё один вариант решения
print("\nЕщё один вариант решения")
def personal_info(**kwargs):
      return kwargs

print(personal_info(name=input("введите имя: "), lastname=input("введите фамилию: "), year=input("введите год рождения: "), city=input("введите город: "), email=input("введите email: "), tel=input("введите телефон: ")))

