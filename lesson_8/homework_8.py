# #Задание1
# print("Задачи по итераторам\nЗадание1")
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# numbers = iter(numbers)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
#
# #Задание2
# print("Задание 2")
# str_1 = "Andrew"
# str_1 = iter(str_1)
# print(next(str_1))
# print(next(str_1))
# print(next(str_1))
# print(next(str_1))
# print(next(str_1))
# print(next(str_1))

# #Задание1
# print("Задачи по теме Генераторы списков (List Comprehensions)\nЗадание1")
# N = int(input("Введи число: "))
# list_1 = [num ** 2 for num in range(1, N + 1)]
# print(list_1)

# #Задание2
# print("Задание 2")
# chet = [i for i in range(-10, 11) if i % 2 == 0]
# print(chet)
#
# #Задание3
# print("Задание 3")
# words  = ["Москва", "Павлово", "Нижний", "Питер"]
# lengths  = [len(word) for word  in words]
# print(lengths)

# #Задание4
# print("Задание 4")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# number = [f"{i} - положительное" if i > 0 else f"{i} - отрицательное" for i in numbers]
# print(number)

#Задание5
print("Задание 5")
objects = [42, "Hello", [1, 2, 3]]

# Убираем строку из итерируемых типов
iterable_types = (list, tuple, dict, set)

is_iterable = [
    type(obj) in iterable_types
    for obj in objects
]

print(is_iterable)  # [False, False, True]