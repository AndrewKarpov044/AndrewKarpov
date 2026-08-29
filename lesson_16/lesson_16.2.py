# """
# map(func, iterable)
# """
# numbers = ["1", "2", "3", "4", "5"]
#
# result = map(int, numbers)
# print(type(result))
# # print(result)
# # print(list(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
#
# cities = ["Москва", "Павлово", "Нижний"]
#
# reverse = map(lambda str_1: str_1[:: -1], cities)
# print(list(reverse))

"""
filter(func, iterable)
"""

# numbers = [2, 3, 5, 4, 1, 2]
#
# even_nums = filter(lambda x: x % 2 == 0, numbers)
# # print(list(even_nums))
# print(next(even_nums))
# print(next(even_nums))
# print(next(even_nums))
#
# """
# zip(iterable1, iterable2, iterable3 ....)
# """
#
# # a = ["fdfds", 31, 32, "fdfere", True]
# # b = ["fdsfe", 21, 64, "ferqr", "fdsfer",  False]
#
#
a = ["fdfds", 31, 32, "fdfere", True]
b = ("fdsfe", 21, 64, "ferqr", "fdsfer",  False)
c = "dsfdfdf"
z = list(zip(a, b, c))
# print(z)

z1, z2, z3 = zip(*z)
print(z1)
print(z2)
print(z3)
