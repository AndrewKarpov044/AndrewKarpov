"""
Итерированные объекты:
строки (str)
списки (list)
кортежи (tuple)
диапазоны чисел (range)
словари (dict)
множества (set)
"""
# numbers = [34, 21, 53, 31, 21, 63, 53, 64, 32, 64]
# it_numbers = iter(numbers)
# print(type(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))

str_1 ="Andrew"
it_str = iter(str_1)
# print(type(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))
# print(next(it_str))

for letter in str_1:
    print(letter)