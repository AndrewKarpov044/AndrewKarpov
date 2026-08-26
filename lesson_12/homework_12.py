#Задание1
print("Лямбда-функции\nЗадание1")
square = lambda a: a ** 2
print(square(10))

#Задание2
print("Задание 2")
chet = lambda b: True if b % 2 == 0 else None
print(chet(2))

#Задание3
print("Задание 3")
words = ["banana", "apple", "cherry", "fdafadfa"]
sort_by_last_letter = sorted(words, key=lambda x: x[:: -1] )
print(sort_by_last_letter)

#Задание1
print("Замыкания\nЗадание1")
def multiply_by(n):
    def multiple(x):
        return x * n
    return multiple
times3 = multiply_by(3)
times5 = multiply_by(5)
print(times3(10))
print(times5(10))

#Задание2
print("Задание 2")
def counter(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
c1 = counter(5)
c2 = counter()

print(c1())
print(c1())
print(c2())
print(c2())
