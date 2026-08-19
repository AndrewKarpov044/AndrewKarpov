N = 5
# result = []
# for i in range(1, N + 1):
#     result.append(i ** 2)

# result = [num ** 2 for num in range(1, N + 1)]

# numbers = [34, 21, 53, 31, 21, 63, 53, 64, 32, 64]
# result_numbers = [num > 35 for num in numbers]
#
# print(result_numbers)

# numbers = [34, 21, 53, 31, 21, 63, 53, 64, 32, 64]
# result_numbers = [num for num in numbers if num > 35]
#
# print(result_numbers)


# numbers = [1, -1, 3, 2, -4, 0]
# # result = []
# # for num in numbers:
# #     if num > 0:
# #         result.append(f"{num} - положительное")
# #     else:
# #         result.append(f"{num} - отрицательное")
# #
# # print(result)
#
# result = [f"{num} - положительное" if num > 0 else f"{num} - отрицательное" for num in numbers]
#
# print(result)

table_multiple = [
    f"{x} * {y} = {x * y}"
    for x in range(1, 10)
    for y in range(1, 10)
]
print(table_multiple)