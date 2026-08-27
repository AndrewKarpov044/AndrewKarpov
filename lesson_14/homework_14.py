# #Задание1
# print("Модули в Python\nЗадание1")
# from math import sqrt, pow
# print(sqrt(64))
# print(pow(5, 3))
#
# #Задание2
# print("Задание 2")
# import random
# print(random.randint(1, 10))
# print(random.choice(["Python", "Java", "C++"]))
#
# #Задание3
# print("Задание 3")
# import my_module
# print(my_module.add(3,5))
# print(my_module.multiple(4,6))
#
# #Задание5
# print("Задание 5")
# import time
# start = time.time()
# time.sleep(1)
# end = time.time()
# print(f"Код выполнялся: {end - start:.4f} сек ")

# #Задание6
# print("Задание 6")
# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)

#Задание7
print("Задание 7")
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()