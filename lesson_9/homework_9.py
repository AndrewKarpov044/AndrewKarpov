# #Задание1
# print("Словари в Python (dict)\nЗадание1")
# frukt = {"apple": 100, "banana": 200, "orange": 300}
# frukt["pineapple"] = 400
# print(frukt)
#
# #Задание2
# print("Задание 2")
# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
# for name, grade in grades.items():
#     if grade >= 4:
#         print(name)
#
# #Задание3
# print("Задание 3")
# capitals = {
#     "Россия": "Москва",
#     "Франция": "Париж",
#     "Германия": "Берлин",
#     "Италия": "Рим",
#     "Испания": "Мадрид",
#     "Великобритания": "Лондон",
#     "США": "Вашингтон",
#     "Япония": "Токио",
#     "Китай": "Пекин",
#     "Индия": "Нью-Дели"
# }
# country = input("Введите название страны: ")
# capital = capitals.get(country)
# if capital:
#     print(f"Столица {country} - {capital}")
# else:
#     print("Такой страны нет")

# #Задание4
# print("Задание 4")
# students = [
#     ("Анна", "Python"),
#     ("Борис", "Java"),
#     ("Виктор", "Python"),
#     ("Галина", "C++"),
#     ("Дмитрий", "Python")
# ]
#
# courses = {}
#
# for name, course in students:
#     # setdefault() возвращает существующий список или создает новый
#     courses.setdefault(course, []).append(name)
#
# print(courses)
#
# #Задание5
# print("Задание 5")
# grades = {
#     "Анна": 5,
#     "Борис": 4,
#     "Виктор": 3,
#     "Галина": 5,
#     "Дмитрий": 2
# }
# min_grade = min(grades.values())
# student = None
# for name, grade in grades.items():
#     if grade == min_grade:
#         student = name
#         break
# if student:
#     grades.pop(student)
# print(grades)
#
#
# #Задание6
# print("Задание 6")
# students = ["Анна", "Борис", "Виктор", "Галина"]
# student_dict = dict.fromkeys(students, 23)
# print(student_dict)

# #Задание7
# print("Задание 7")
# exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
# currency = input("Введите валюту (USD, EUR или GBP): ")
# if currency in exchange_rates:
#     print(f"Курс {currency}: {exchange_rates[currency]}")
# else:
#     print("Неизвестная валюта")
#     exchange_rates[currency] = None
#     print(f"Валюта {currency}: добавлена в словарь со значением None")
#
# print("\nОбновленный словарь курсов:")
# print(exchange_rates)

#Задание8
print("Задание 8")
dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
dict1.update(dict2)
print(dict1)

#Задание1
print("Кортежи в Python\nЗадание1")
i = (1, 1.312, "fdfa", True, [1, 2, 3])
print(i[1])
print(i[-1][-1])

#Задание2
print("Задание 2")
nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
print(nums.count(4))
print(nums.index(7))

#Задание3
print("Задание 3")
lst = ["Python", "Java", "C++", "JavaScript"]
print(lst)
print(type(nums))
lst_1 = tuple(lst)
print(lst_1)
print("C++" in lst_1)

#Задание4
print("Задание 4")
num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(num[0:3])
print(num[-3:])
print(num[:: 2])

#Задание5
print("Задание 5")
i = ({"name": "Python", "age": 18}, [1, 2, 3, 4, 5])
i[1].append(6)
print(i)