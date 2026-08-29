# x = "Строка"
# print(isinstance(x, str))
# print(isinstance(x, int))

x = True

print(isinstance(x, bool))
print(isinstance(x, int))
print(isinstance(x, str))


x = 2.4
print(isinstance(x, (bool, int, float)))

# x = True
#
# print(type(x) is bool)
# print(type(x) is int)

numbers = [3, 2, 3, "fdfee", 12.31, "fsferewtew"]
result = 0
for x in numbers:
    if isinstance(x, (float, int)):
        result += x
print(result)


