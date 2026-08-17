# #Задание1
# print("Условный оператор\nЗадание1")
# x = int(input("Введите число: "))
# if x > 0:
#     print("Число положительное")
# elif x < 0:
#     print("Число отрицательное")
# else:
#     print("Число равно нулю")
#
# #Задание2
# print("Задание 2")
# x = int(input("Введите число: "))
# if x % 2 == 0:
#     print("Число чётное")
# else:
#     print("Число нечётное")
#
# #Задание3
# print("Задание 3")
# x = int(input("Введите число: "))
# if 0 > x < 11:
#     print("Число в диапазоне")
# else:
#     print("Число вне диапазона")
from lession_1.homework_1 import password

# #Задание4
# print("Задание 4")
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# if a < b:
#     a, b = b, a
# print(a, b)

# #Задание5
# print("Задание 5")
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# if a < b:
#     print(a)
# else:
#     print(b)
#
# #Задание6
# print("Задание 6")
# marks = [3, 4, 5, 2, 5, 4]
# if marks in 2:
#     print("Есть неудовлетворительная оценка")
# else:
#     print("Все оценки положительные")

# #Задание7
# print("Задание 7")
# x = int(input("Введите число: "))
# if x % 3 == 0 and x % 5 == 0:
#     print("Число делиться на 3 и 5")
# elif x % 3 == 0 and x % 5 != 0:
#     print("Число делиться только на 3")
# elif x % 3 != 0 and x % 5 == 0:
#     print("Число делиться только на 5")
# else:
#     print("Число не делится на 3 и 5")
#
# #Задание8
# print("Задание 8")
# password = int(input("Введите пароль: "))
# if password == "admin123":
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# #Задание9
# print("Задание 9")
# amount = int(input("Введите сумму покупки: "))
# if amount >= 5000:
#     amount = amount * 0.9
#     print("У вас скидка 10%")
# elif amount >= 1000:
#     amount = amount * 0.95
#     print("У вас скидка 5%")
# else:
#     print("Скидки нет")
# print(amount)

# #Задание10
# print("Задание 10")
# year = int(input("Введите год: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Год високосный")
# else:
#     print("Год не високосный")
#
# #Задание1
# print("Вложенные условия и elif\nЗадание1")
# a = int(input("Введите число (1 - 5): "))
# if a == 5:
#     print("Оценка отлично!")
# elif a == 4:
#     print("Оценка хорошо!")
# elif a == 3:
#     print("Оценка удовлетворительно")
# elif 2 == a == 1:
#     print("Оценка неудовлетворительно")
# else:
#     print("Некорректная оценка")

# #Задание2
# print("Задание 2")
# clock = int(input("Введите число (0 - 23): "))
# if 6 <= clock <= 11:
#     print("Сейчас утро")
# elif 12 <= clock <= 17:
#     print("День")
# elif 18 <= clock <= 21:
#     print("Вечер")
# elif 22 <= clock <= 23 or 0 <= clock <= 5:
#     print("Ночь")
# else:
#     print("Некорректное время")
#
# #Задание3
# print("Задание 3")
# temp =  int(input("Введите температуру: "))
# if temp < -10:
#     print("Очень холодно")
# elif -10 > temp <= 0:
#     print("Холодно")
# elif 1 >= temp <= 10:
#     print("Прохладно")
# elif 11 >= temp <= 25:
#     print("Тепло")
# else:
#     print("Очень жарко")
#
# #Задание4
# print("Задание 4")
# year = int(input("Введите год: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Год високосный")
# else:
#     print("Год не високосный")

# #Задание5
# print("Задание 5")
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# op = input("Введите операцию: ")
# if op == "+":
#     print(a + b)
# elif op == "-":
#     print(a - b)
# elif op == "*":
#     print(a * b)
# elif op == "/":
#     if b != 0:
#         print(a / b)
#     elif b == 0:
#         print("Ошибка: деление на ноль!")
# else:
#     print("Некорректная операция")

# #Задание1
# print("Тернарный оператор\nЗадание1")
# a = int(input("Введите число: "))
# result = "Чётный" if a % 2 == 0 else "Нечётный"
# print(result)

# #Задание2
# print("Задание 2")
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# res = "Наибольший а" if a > b else "Наибольший b"
# print(res)

# #Задание3
# print("Задание 3")
# num = int(input("Введите число: "))
# res = "Положительное" if num > 0 else "Отрицательное" if num < 0 else "Нулем"
# print(res)

# #Задание4
# print("Задание 4")
# age = int(input("Введите возраст: "))
# open = "Вход разрешен" if age >= 18 else "Вход запрещен"
# print(open)
#
# #Задание5
# print("Задание 5")
# sum = int(input("Введите число: "))
# final_sum = sum * 0.9 if sum >= 5000 else sum
# print(final_sum)