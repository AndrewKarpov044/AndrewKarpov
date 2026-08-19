"""
set
"""

# set_1 = {1, 2, 3, 4, 5, True, "sdfdaf", (9, 5)}
# print(set_1)
# print(type(set_1))

"""
Изменяемые типы данных
list списки
dict словари
set множества
"""

"""
Не изменяемые типы данных
int числа
float нецелые числа
str строки
tuple (1,2,3)
bool булевые значения
"""

# set3 = set()
# set4 = {}# тут создаться словарь, а не множество

lst = [1, 2, 3, 4, 5, 6, (1, 2), (1, 2)]
# print(set(lst))
# str1 = "qweqweqwe"
# print(set(str1))
#
# range_1 = range(5)
# print(set(range_1))
#
set_2 = set(lst)
# print(len(set_2))
# print((1, 2) in set_2)
# for i in set_2:
#     print(i)
# ir = iter(set_2)
# print(next(ir))
#
# set_2.add(213121)
# print(set_2)
#
# set_2.update([1312, 21232, 3, 4, 5, 5])
# print(set_2)
#
# set_2.discard(213121)
# print(set_2)

# set_2.remove(213121)
# print(set_2)

# set_2.clear()
# print(set_2)

set_6 = {1, 2, 3, 4, 5}
set_7 = {4, 5 ,6, 7, 8}
set_8 = {9, 10}
# res = set_3 & set_4
# res = set_3.intersection(set_4)
# print(res)
# set_3 &= set_4
# set_3 &= set_5
# print(set_3)

# res = set_3 | set_4
# # res = set_3.union(set_4)
# set_6 |= set_7
# print(set_6)

# res = set_6 - set_7
# res = set_6.difference(set_7)
# set_6 -= set_7
# res = set_6 ^ set_7
# res = set_6.symmetric_difference(set_7)
# set_6 ^= set_7
print(set_6 != set_7)

