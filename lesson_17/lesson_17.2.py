"""
all()
any()
"""
# lst = [True, True, False]
# print(all(lst))
# print(any(lst))

lst_1 = [1, 2, 52, 31, "fwfqewr", ""]
print(all(lst_1))
print(bool(""))
print(bool(0))


"""
bool Возвращает false если 
0
""
{}
[]
"""

# lst_2 = ["Andrew", "Daniil", "Victor", "Sergey"]
nums = [1, 2, 5, 2, 1, 4, 2]
nums_bool = [x % 2 == 0 for x in nums]
print(nums)
print(nums_bool)
print(any(nums_bool))
if any(nums_bool):
    pass


print(all(nums_bool))
