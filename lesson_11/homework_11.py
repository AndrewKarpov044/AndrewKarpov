# #Задание1
# print("Функции в Python\nЗадание1")
# def hi(name):
#     print(f"Привет, {name}! Добро пожаловать!")
# hi("Andrew")
#
# #Задание2
# print("Задание 2")
# def square(num):
#     return num ** 2
# print(square(5))
#
# #Задание3
# print("Задание 3")
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(5))
# print(is_even(4))
#
# #Задание4
# print("Задание 4")
# def repeat_string(text, times):
#     return text * times
# print(repeat_string("python", 2))
# print(repeat_string("python", 3))
#
# #Задание5
# print("Задание 5")
# def add(a, b):
#     res = a + b
#     return res
# print(add(1, 2))
#
# #Задание6
# print("Задание 6")
# def get_max(a, b, c):
#     if b < a > c:
#         return a
#     elif a < c > b:
#         return c
#     else:
#         return b
# print(get_max(10, 5, 4))
#
# def get_max(a, b, c):
#     return max(a, b, c)
#
# print(get_max(10, 25, 7))


#Задание7
print("Задание 7")
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Неизвестный оператор"
print(calculate(4, 5, operator="*"))
print(calculate(4, 5, operator="+"))

#Задание8
print("Задание 8")
def reversre_string(word):
    return word[::-1]
print(reversre_string("Python"))

#Задание9
print("Задание 9")
def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_case:
        s1 = s1.lower()
        s2 = s2.lower()
    if ignore_spaces:
        s1 = s1.replace(" ", "")
        s2 = s2.replace(" ", "")
    return s1 == s2
print(compare_strings("Python", "Python", ignore_case=False))

#Задание10
print("Задание 10")
def summarize(*args):
    total = 0
    for value in args:
        if isinstance(value, (int, float)):
            total += value
    return total

print(summarize(1, 2, 3))

#Задание11
print("Задание 11")


def create_profile(name, age, **extra):
    print("Профиль пользователя:")
    print(f"Имя: {name}")
    print(f"Возраст: {age}")

    if extra:
        print("Дополнительная информация:")
        for key, value in extra.items():
            print(f"{key}: {value}")


create_profile("Иван", 30, city="Москва", job="Инженер")


#Задание12
print("Задание 12")


def process_orders(*orders, discount=0):
    total = sum(orders)
    print(f"Сумма заказа: {total}")

    if discount > 0:
        discounted = total * (1 - discount / 100)
        print(f"С учетом скидки: {discounted}")
    else:
        print(f"С учетом скидки: {total}")


print(process_orders(100, 200, 300, discount=10))

#Задание13
print("Задание 13")
def merge_lists(*lists):
    a = lists
    print(a)
print(merge_lists([1, 2], [3, 4], [5, 6]))