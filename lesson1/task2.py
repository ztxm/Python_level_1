"""
2. Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

time_in_seconds = int(input("Введите время в секундах: "))
if time_in_seconds <= 0:
    print("Ошибка, время в скундах должно быть больше 0")
else:
    hours = time_in_seconds // (60 * 60)
    sec = time_in_seconds % (60 * 60)
    minutes = sec // 60
    seconds = sec % 60
    print(f"Время в формате чч:мм:сс = {hours}:{minutes}:{seconds}")