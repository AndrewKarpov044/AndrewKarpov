#Задание1
print("Методы строк и print()\nЗадание1")
s = "Python для автоматизации"
print(s.upper())
print(s.lower())

#Задание2
print("Задание 2")
msg = "абракадабра"
# print(msg.find("ра"))
print(msg.count("а", 3))

#Задание3
print("Задание 3")
print(msg.find("ка"))
print(msg.find("а"))
print(msg.find("xyz"))

#Задание4
print("Задание 4")
text = "Я изучаю Java"
text2 = text.replace("Java", "Python")
print(text2)
print(text2.replace(" ", ''))

#Задание5
print("Задание 5")
text3 = "Python"
text4 = "22131"
text5 = "123141gddtr"
print(text3.isalpha())
print(text4.isdigit())
print(not(text5.isdigit()))

#Задание6
print("Задание 6")
code = "42"
print(code.rjust(5, "0"))
print("text".rjust(10,"*"))

#Задание7
print("Задание 7")
frukt = "яблоко,груша,банан"
apple, orange, banana = frukt.split(",")
print(apple)
print(orange)
print(banana)
programm = "Python;Java;C++"
p, j, c = programm.split(";")
print(p)
print(j)
print(c)

#Задание8
print("Задание 8")
text = ["Привет", "мир", "!"]
print(" ".join(text))
text2 = ["apple", "banana", "cherry"]
print(",".join(text2))

#Задание9
print("Задание 9")
text3 = " Python "
print(text3.lstrip())
print(text3.rstrip())
print(text3.strip())

#Задание10
print("Задание 10")
text = "программирование"
print(text.capitalize())
print(text.count("р"))
print(text[:: -1])


#Задание1
print("Спецсимволы\nЗадание1")
text = "Hello\nPython"
print(text)

#Задание2
print("Задание 2")
t = "Python\tAutomation"
print(t)

#Задание3
print("Задание 3")
path = "C:\\new\\test.txt"
print(path)
print("\"Марка вина \"Ягодка\"")

#Задание4
print("Задание 4")
path = r"C:\new\test.txt"
print(path)

#Задание5
print("Задание 5")
s = "Hello\b World"
print(s)
s = "Hello\fPython"
print(s)


#Задание1
print("Форматирование строк\nЗадание1")
name = "Andrew"
age = 23
print("My name is " + name + " and I am " + str(age) + " years old")
print(f"My name is {name} and I am {age} years old")

#Задание2
print("Задание 2")
print("Меня зовут {name}, мне {age} лет".format(name=name, age=age))

#Задание3
print("Задание 3")
city = "Москва"
year = 2026
print(f"Сегодня {year + 5} год, и я живу в городе {city}")

#Задание4
print("Задание 4")
age = 23
print(f"Дважды мой возраст {age * 2}")
print(f"My name is {name.upper()} and I am {age} years old")

#Задание5
print("Задание 5")
curs = 92.5
print(f"Курс валют: 1 доллар = {curs}")
print(f"Квадрат числа 7 = {7 ** 2}")
