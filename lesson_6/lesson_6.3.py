a = 18
b = 15

# if a > b:
#     res = a
#     print("a больше b")
# elif b > a:
#     res = b
#     print("b больше a")
# else:
#     print("Числа равны")

if a > b:
    res = a
else:
    res = b
print(res)

res = a + 10 if a > b else b
print(res)