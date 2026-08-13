#Задание1
print("Задачи на input() и print()\nЗадание1")
print("Привет, мир!")
print(5, 10, 15)
print(10 + 15)

#Задание2
print("Задание2")
print(1, 2, 3, sep="&")
print("Python", end=" ")
print("лучший язык")

#Задание3
print("Задание3")
x = 3.14
y = -8
print(f"Координаты точки {x}; {y}")
name = input("Name ")
age = input("Age ")
print(f"Your name is {name}, and your age is {age}")

#Задание4
print("Задание4")
name1 = input("name")
print(f"Hellow, {name1}")

#Задание5
print("Задание5")
a = input("Введите первое число ")
b = input("Введите второе число ")
print(a + b)
c = int(input("Введите число чтобы возвести в квадрат "))
print(c ** 2)

#Задание1
print("Булевые значения\nЗадание1")
print(5 > 3)
print(10 < 2)
print(7 == 7)
print(6 != 8)
print(4 >= 4)
print(9 <= 3)
print(type(8 > 12))

#Задание2
print("Задание2")
x = 15
print(x % 2 == 0)
print(x % 5 == 0)
print((x % 5 == 0) and (x % 3 == 0))

#Задание3
print("Задание3")
y = 4.5
print(1 < y > 10)
print((0 < y > 5) or (10 < y > 15))
print(not(y<5))

#Задание4
print("Задание4")
x = 10 - 5
print(x == 5 or 2 > x > 10)
print(not(4 == x >= 5))
print(x % 3 == 0 or not(4 < x > 2))
print(not(10 > 5 or 3 < 1))

#Задание5
print("Задание5")
print(bool(0))
print(bool(-5))
print(bool(3.14))
print(bool(""))
print(bool("Python"))
print(bool(" "))

#Задание6
print("Задание6")
n = 10
print(n >= 0)
print(n % 2 == 0)
print(n % 3 == 0)

#Задание1
print("Срезы строк")
print("Задание 1")
s = "Программирование"
print(s[0])
print(s[-1])
print(s[2])
print(s[-2])

#Задание2
print("Задание 2")
# print(s[100])
print(len(s[-1]))

#Задание3
print("Задание 3")
s1 = s[:6]
print(s1)
s2 = s[5:]
print(s2)
s3 = s[3:7]
print(s3)
print(s[1:: 2])
print(s[:: -1])

#Задание4
print("Задание 4")
print(s[0:: 3])
print(s[:: -2])

#Задание5
print("Задание 5")
s4 = "Д" + s[2:]
print(s4)

#Задание6
print("Задание 6")
word = "abcdefgh"
print(word[2:5])
print(word[:: -1])
print(word[1:7])