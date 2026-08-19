# sum_1 = 1 + 2 + 3 + 4 + 5
# print(sum_1)

# num = 1000
# sum_2 = 0
# i = 1
# while i <= 1000:
#     sum_2 += i
#     i += 1
#
# print(sum_2)

# input_password = input("Enter your password: ")
# correct_password = "Пароль12345"
#
# while input_password != correct_password:
#     print("Пароль не верен, введите ещё раз")
#     input_password = input("Enter your password: ")
#
# print("Пароль верен")

# input_password = input("Enter your password: ")
# correct_password = "Пароль12345"
# counter = 1
#
# while input_password != correct_password:
#     print(f"Пароль введен не правильно {counter} раз, введите ещё раз")
#     input_password = input("Enter your password: ")
#     counter += 1
#     if counter == 3:
#         print(f"Пароль введён не правильно {counter} раза, программа завершена")
#         break
#
# print("Пароль верен")

# numbers = [23, 43, 75, 33, 80, 51, 62]
# result = []
# i = 0
# while True:
#     if numbers[i] % 2 == 0:
#         result.append(numbers[i])
#     i += 1
#     if i == len(numbers):
#         break
# print(result)

num = 1
res_sum = 0
while num != 0:
    input_num = input("Введите целое число или 0 для выхода:")
    if not input_num.isdigit():
        print("Введено не число, перезапустите программу")
        break
    num = int(input_num)

    if num % 2 == 0:
        continue
    res_sum += num
else:
    print(res_sum)
