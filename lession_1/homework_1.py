#1
from itertools import count

name = "Andrew Karpov"
age = 23
height = 188.0
print("Имя", name)
print("Возраст", age)
print("Рост", height)

#2
x = 10
x = 25.5
x = "Python"
print(x)
print(type(x))

#3
a = 7
b = a
print(a, b)
a = 10
print(a, b)

#4
x = y = z = 100
print(x, y, z)
print(id(x), id(y), id(z))
x, y, z = 100, 101, 102
print(x, y, z)
print(id(x), id(y), id(z))

#5
a = 5
b = 10
a, b = 10, 5
print(a, b)

#6
import keyword
print(keyword.kwlist)

#7
var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1), type(var2), type(var3))
var1 = "Hello"
print(type(var1))

#8
login = "lion3322"
password = 23141231
email = "ivanov@mail.ru"
country = "USA"
numbers = 41234121
print(type(login),type(password),type(email),type(country),type(numbers))
переменная = 10
print(переменная)
