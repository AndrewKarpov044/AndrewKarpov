#Задание1
print("Выражения-генераторы\nЗадание1")
def filter_strings(items):
    for item in items:
        if isinstance(item, str):
            yield item

my_list = ["Python", 123, "Java", 456, "C++", 789]

gen = filter_strings(my_list)

print(" ".join(gen))

#Задание2
print("Задание 2")
import random

gen = (random.randint(1, 100) for i in range(10))

print(f"Максимально число: {max(gen)}")

#Задание3
print("Задание 3")


