a = 12
b = 32.21
c = 89

print(a, b, c, sep='|', end=' ')
print(a, b, c, sep='|')
print("Результат умножения числа", a, "и числа", b, 'равен', a * b)
print(f"Результат умножения числа {a} и числа {b}  равен {a * b}") #f-string

a = int(input())
print(type(a))

x = float(input("Введите длину прямоугольника: "))
y = float(input("Введите шириину прямоугольника: "))
print(f"Периметр: {2 * (x + y)}")