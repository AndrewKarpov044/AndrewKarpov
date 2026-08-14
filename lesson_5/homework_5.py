#Задание1
print("Списки\nЗадание1")
cities = ["Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "fgds", True, 213.21]

#Задание2
print("Задание 2")
print(cities[0])
print(numbers[-1])

#Задание3
print("Задание 3")
numbers[1] = 10
mixed[-1] = "Python"

#Задание4
print("Задание 4")
print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

#Задание5
print("Задание 5")
lst =  [1, 2, 3] + [4, 5]
print(lst)
print(["Python", "is", "awesome"] * 3)

#Задание6
print("Задание 6")
print(3 in numbers)
print("Москва" in cities)
print([1, 2] in mixed)

#Задание7
print("Задание 7")
print(numbers)
numbers.pop(2)
print(numbers)
print(cities)
del cities[-1]
print(cities)

#Задание8
print("Задание 8")
lst = list("Python")
print(lst)
print(max(lst))
print(min(lst))

#Задание1
print("Срезы списков\nЗадание1")
city = ["Москва", "Владивосток", "Казань", "Павлово", "Нижний Новгород"]
city2 = city[:]
print(id(city))
print(id(city2))

#Задание2
print("Задание 2")
print(city[1:3])
print(city[2:])
print(city[:3])
print(city[:])
print(city[-1:])

#Задание3
print("Задание 3")
print(city[:])
print(city[:: 2])
print(city[:: -2])

#Задание4
print("Задание 4")
city[1::2] = ["Город"] * len(city[1::2])
print(city)
city[1:3] = "Волгоград", "Омск"
print(city)
#
# #Задание5
# print("Задание 5")
# numbers = [1, 2, 3]
# numbers2 = [4, 5, 6]
# numbers3 = numbers + numbers2
# print(numbers3)
# text2 = ["Python", "rocks"]
# text3 = text2 * 2
# print(text3)

#Задание6
print("Задание 6")
print([1, 2, 3] == [1, 2, 3])
print([10, 5, 3] > [5, 10, 3])
print([1, 2, 3] == [1, 2, "abc"])

#Задание7
print("Задание 7")
chars = list("Python")
print(max(chars))
print(min(chars))

#Задание1
print("Методы списков\nЗадание1")
numbers = [5, 10, 15]
numbers.append(20)
numbers.insert(1, 7)
numbers.append("Python")
print(numbers)

#Задание2
print("Задание 2")
numbers.remove(10)
numbers.pop()
numbers.pop(1)
print(numbers)
numbers.clear()
print(numbers)

#Задание3
print("Задание 3")
letters = ["a", "b", "c"]
letters2 = letters.copy()
letters3 = list(letters)
print(id(letters2))
print(id(letters3))

#Задание4
print("Задание 4")
marks = [2, 3, 5, 3, 4, 5, 2, 3]
print(marks.count(3))
print(6 in marks)
print(marks.index(5))

#Задание5
print("Задание 5")
nums = [8, 2, 5, 1, 7]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.sort(reverse=False)
print(nums)

#Задание6
print("Задание 6")
cities = ["Москва", "Владивосток", "Казань", "Павлово", "Нижний Новгород"]
cities.sort()
print(cities)
cities = ["Москва", "Владивосток", "Казань", "Павлово", "Нижний Новгород"]
cities2 = sorted(cities)
print(cities2)

#Задание7
print("Задание 7")
chars = list("programming")
print(chars.count("g"))
chars.reverse()
print(chars)
chars.sort()
print(chars)

#Задание1
print("Вложенные списки (массивы)\nЗадание1")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix)
print(matrix[1])
print(matrix[2][0])

#Задание2
print("Задание 2")
matrix[0] = [0, 0, 0, 0]
matrix[1][-1] = "python"
print(matrix)