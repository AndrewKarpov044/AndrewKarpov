# #Задание1
# print("Задачи по уроку Цикл while\nЗадание1")
# num = int(input("Введите число: "))
# i = 1
# while num >= i:
#     print(i)
#     i += 1
from lession_1.homework_1 import password

# #Задание2
# print("Задание 2")
# num2 = int(input("Введите число: "))
# i = 1
# sum_1 = 0
# while num2 >= i:
#     if i % 2 == 0:
#         sum_1 += i
#     i += 1
# print(f"Сумма чётных чисел от 1 до {num2} = {sum_1}")

# #Задание3
# print("Задание 3")
# num = input("Введите число: ")
# count = 0
# i = 0
# while i < len(num):
#     count += 1
#     i += 1
# print(f"Цифр: {count}")

# # #Задание4
# # print("Задание 4")
# num = input("Введите число: ")
# max_digit = 0
# i = 0
# while len(num) >= i:
#     digit = int(num[i])
#     if digit > max_digit:
#         max_digit = digit
#     i += 1
# print(max_digit)

# # #Задание5
# print("Задание 5")
# password_1 = str(input("Введите пароль: "))
# correct_password = "qwerty123"
#
# while password_1 != correct_password:
#     print("Неверный пароль")
#     password_1 = str(input("Введите пароль: "))
#
# print("Доступ разрешен")

# #Задание1
# print("Задачи по уроку "Операторы break, continue и else в цикле while"\nЗадание1")
# print("Задание 1")
# list_1 = [23, 21, 23, 55, 73, 33, 53]
# i = 0
# while i < len(list_1):
#     if list_1[i] % 2 == 0:
#         print(list_1[i])
#         break
#     i += 1
# else:
#     print("Четное число не найдено")

# # #Задание2
# print("Задание 2")
# total_sum = 0
# while True:
#     nun = int(input("Введите число: "))
#     if nun == 0:
#         break
#     if nun < 0:
#         continue
#     total_sum += nun
#     print(f"Текущая сумма {total_sum}")
# print(f"Итоговая сумма положительных чисел {total_sum}")

# # #Задание3
# print("Задание 3")
# a = int(input("Введите начало диапазона (a): "))
# b = int(input("Введите конец диапазона (b): "))
# if a > b:
#     a, b = b, a
# i = a
# print(f"Нечетные числа в диапазоне [{a}, {b}]:")
# while i <= b:
#     if i % 2 == 0:  # если число четное
#         i += 1
#         continue  # пропускаем его
#     print(i, end=" ")
#     i += 1

# # #Задание4
# print("Задание 4")
# N = int(input("Введите число для проверки: "))
#
# # Проверка на простоту
# i = 2
# while i < N:
#     if N % i == 0:  # нашли делитель
#         print(f"{N} не является простым, так как делится на {i}")
#         break
#     i += 1
# else:
#     # Этот блок выполняется, если break НЕ сработал
#     print(f"{N} является простым числом")

# # #Задание5
# print("Задание 5")
# max_number = None  # переменная для хранения максимального числа
#
# while True:
#     user_input = input("Введите число (0 для выхода, Enter для отмены): ")
#
#     # Проверка на пустую строку (пользователь отказался)
#     if user_input == "":
#         print("Ввод отменен пользователем")
#         break
#
#     # Преобразуем в число
#     num = int(user_input)
#
#     # Проверка на выход
#     if num == 0:
#         print("Выход из программы")
#         break
#
#     # Обновляем максимум
#     if max_number is None or num > max_number:
#         max_number = num
#
# # Вывод результата
# if max_number is None:
#     print("Не было введено ни одного числа")
# else:
#     print(f"Наибольшее введенное число: {max_number}")

# # #Задание1
# # print(Задачи по уроку "Цикл for в Python – основы и применение"\nЗадание1")
# # print("Задание 1")
# city = ["Москва", "Питер", "Калининград", "Кострома",]
# for word in city[:: -1]:
#     print(word)

# # #Задание2
# print("Задание 2")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range (len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i] = 0
# print(numbers)

# #Задание3
print("Задание 3")
N = int(input("Введите число: "))
power = []
for i in range(N + 1):
    power.append(2 ** i)
print(f"Степени двойки от 2^0 до 2^{N}:")
print(power)

# #Задание4
print("Задание 4")
A = int(input("Введите начало (A): "))
B = int(input("Введите конец (B): "))
K = int(input("Введите шаг (K): "))

print(f"Числа от {A} до {B} с шагом {K}:")
for i in range(A, B + 1, K):
    print(i, end=" ")