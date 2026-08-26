# def get_number(x, y, z=5):
#     print("x = ", x)
#     print("y = ", y)
#     print("z = ", z)

# x1 = 1
# y1 = 2
# z1 = 3

# get_number(x1, y1, z1)
# get_number(y = x1, z = y1, x = z1)

# get_number(1, 2, 2)

# def get_lowwer_upper_str(str_1, lower = True, upper = False):
#     if lower:
#         return str_1.lower()
#     elif upper:
#         return str_1.upper()
#     else:
#         return str_1
# print(get_lowwer_upper_str("Andrew"))
# print(get_lowwer_upper_str("Andrew", lower = False))
# print(get_lowwer_upper_str("Andrew", lower = False, upper = True))

def ad_value(value, lst=[]):
    if not lst:
        lst = []
    lst.append(value)
    return lst
print(ad_value(1))
print(ad_value(4, []))
print(ad_value(2))
