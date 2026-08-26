"""
DRY - Don"t Repeat Yourself
"""
print("Вывод в консоль")

# func = print
# func("Вывод в консоль")
# print(id(print()))
# print(id(func()))
#
# def print_text(add_text):
#     text = f"Текст для печати: {add_text}"
#     print("add_text", id(add_text))
#     print(text)
#
#
# str_1 = "Курс от Андрея"
# print("str_1",id(str_1))
# print_text("Курс от Андрей")
# # print(print_text())
#
# def summarizi_two(x, y):
#     res_sum = x + y
#     return res_sum
#     print("Полсе return")
# print(summarizi_two(1, 2))
# def mulply_two(x, y):
#     res_mult = x * y
#     return res_mult
# print(mulply_two(1, 2))
#
# def common(x, y):
#     return summarizi_two(x, y), mulply_two(x, y)
# print(common(4, 5))
#
def is_negative(x):
    return x < 0
# print(is_negative(1))

lst = [1, 2, 0, -2, -1, 2, 5]
for item in lst:
    if is_negative(item):
        print(item, end= " ")