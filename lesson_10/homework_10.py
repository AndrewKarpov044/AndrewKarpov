# #Задание1
# print("Множества в Python\nЗадание1")
# set_1 = {"Python", "JavaScript", "C++", 21, 412, 534}
# set_1.add("Python")
# print(set_1)


# #Задание2
# print("Задание 2")
# set_1 = {"Москва", "Нижний", "Павлово", "Москва"}
# print(set_1)
#
# #Задание3
# print("Задание 3")
# set_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set_2.remove(5)
# print(set_2)
# set_2.discard(15)
# print(set_2)

# #Задание4
# print("Задание 4")
# set_3 = set("abrakadabra")
# print(set_3)
#
# #Задание5
# print("Задание 5")
# set_1 = set()
# set_1.add(10)
# set_1.add("hello")
# set_1.add((1, 2, 3))
# print(set_1)

# #Задание6
# print("Задание 6")
# set_A = {1, 2 ,3 ,4 ,5}
# set_B = {4, 5, 6, 7, 8}
# print("Пересечение:", set_A & set_B)              # {4, 5}
# print("Объединение:", set_A | set_B)              # {1, 2, 3, 4, 5, 6, 7, 8}
# print("Разность A - B:", set_A - set_B)           # {1, 2, 3}
# print("Разность B - A:", set_B - set_A)           # {6, 7, 8}
# print("Симметричная разность:", set_A ^ set_B)   # {1, 2, 3, 6, 7, 8}

# #Задание7
# print("Задание 7")
# even_numbers = {1, 3, 5, 7, 9}
# odd_numbers = {2, 4, 6, 8, 10}
# intersection = even_numbers & odd_numbers
# print(intersection)
# union = even_numbers | odd_numbers
# print(union)

# #Задание8
# print("Задание 8")
# python_students = {"Анна", "Иван", "Мария", "Сергей"}
# java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
# print("Записаны на оба курса", python_students & java_students)
# print("Записаны только на один курс", python_students ^ java_students)
# print("Записаны хотя бы на один курс", python_students | java_students)

# #Задание9
# print("Задание 9")
# text1 = set("программирование")
# text2 = set("автоматизация")
# print("Общие буквы", text1 & text2)
# print("Есть только в первом слове", text1 - text2)
# print("Уникальные буквы у каждого слова", text1 ^ text2)

# #Задание1
# print("Генераторы множеств и словарей\nЗадание1")
# set_1 = {x ** 2 for x in range(10) if x % 2 == 0}
# print(set_1)

# #Задание2
# print("Задание 2")
# words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
# set_1 = {x.upper() for x in words}
# print(words)
# print(set_1)

# #Задание3
# print("Задание 3")
# grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
# set_1 = {name: "Отлично" if grade >= 80 else "удовлетворительно"
#           for name, grade in grades.items()}
# print(set_1)

#Задание4
print("Задание 4")
text = {"Python", "automation", "programming", "testing"}
result = {word: len(word) for word in text}
print(result)

#Задание5
print("Задание 5")
n = 10
# Создаем вложенный словарь с множествами квадратов
result = {
    key: {i**2 for i in range(1, key + 1)}
    for key in range(1, n + 1)
}
print("Результат для n = 10:")
print(result)