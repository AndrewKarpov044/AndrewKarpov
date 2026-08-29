# # #Задание1
# # print("Чтение и запись данных из файлов\nЗадание1")
# file = "data.txt"
# # file_text = open(file = file, encoding= 'utf-8')
# # text = f.read()
# # print(text)
# #
# # #Задание2
# # print("Задание 2")
# # f.seek(0)
# # text = f.readline()
# # print(text)
# #
# # #Задание3
# # print("Задание 3")
# # f.seek(0)
# # text = f.read(10)
# # print(text)
# #
# # #Задание4
# # print("Задание 4")
# # f.seek(0)
# # with f as f:
# #     lines = f.readlines()
# # print(lines)
#
# # #Задание5
# # print("Задание 5")
# # with open(file = "data.txt", encoding= 'utf-8') as f:
# #     for line in f:
# #         print(f"Строка: {line.strip()}")
#
# #Задание6
# print("Задание 6")
# with open(file = "data.txt", encoding= 'utf-8') as f:
#     f.seek(0)
#     first_read = f.read(6)
#     print(first_read)
#     f.seek(0)
#     second_read = f.read(6)
#     print(second_read)
#
#
# #Задание7
# print("Задание 7")
# import os
# size = os.path.getsize("data.txt")
# print(f"Размер файла: {size} байт")
#
# #Задание8
# print("Задание 8")
# with open("data.txt", encoding= 'utf-8') as f:
#     f.seek(0)
#     print(f.read())

# #Задание9
# print("Задание 9")
# try:
#     f = open("data.txt", encoding= 'utf-8')
#     print("Файл открыт")
#     try:
#         print(f.read())
#     finally:
#         f.close()
#         print("Файл закрыт")
# except FileNotFoundError:
#     print("Файл не найден")

# #Задание10
# print("Задание 10")
# # #Задание1
# # print("Чтение и запись данных из файлов\nЗадание1")
# file = "data.txt"
# try:
#     f = open(file=file, encoding='utf-8')
#     print("Файл открыт")
#     text = f.read()
#     print(text)
# finally:
#     print("Файл закрыт")
#     f.close()

# #Задание11
# print("Задание 11")
# try:
#     with open("data.txt", encoding= 'utf-8') as f:
#         for line in f:
#             print(line.strip())
# except FileNotFoundError:
#     print("Ошибка: Файл не найден")
# finally:
#     print("Файл закрыт")

#Задание12
print("Задание 12")
try:
    with open("numbers.txt", encoding= 'utf-8') as f:
        total = 0
        for line in f:
            number = int(line.strip())
            total += number
        print(f"Сумма чисел: {total}")
except FileNotFoundError:
    print("Файл не найден")

#Задание13
print("Задание 13")
import datetime

with open('log.txt', 'a', encoding='utf-8') as file:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{current_time} Запуск программы\n")
    
print(f"Запись в лог добавлена: {current_time}")