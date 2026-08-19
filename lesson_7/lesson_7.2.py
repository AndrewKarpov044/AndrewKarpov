# numbers = [23, 43, 75, 33, 80, 51, 62]
# for number in numbers:
#     print("Печатаем",number)

# for letter in "Андрей":
#     print("Буква",letter)

# numbers = [23, 43, 75, 33, 80, 51, 62]
# for number in numbers:
#     number  = 0
#
# print(numbers)

# numbers = [23, 43, 75, 33, 80, 51, 62]
# for i in range (len(numbers)):
#     numbers[i] = 0
#
# print(numbers)

words = ["Привет,", "Андрей", "Как", "дела?"]
result_str = ""
for word in words:
    result_str += word + " "
print(result_str.lstrip())