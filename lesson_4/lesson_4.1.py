s = "Андрей Карпооов"

s1 = s.lower()
s2 = s.upper()
print(s1)
print(s2)
print(s)

print(s.count("Андрей", 0, 6))

print(s.find("е"))
print(s.rfind("о"))
print(s.index("р"))
print(s.replace("о", "а", 2))
print(s)
print(s.replace(" ", ""))
print(s.replace(" ", "").isalpha())
# a = "23123131"
# print(a.isdigit())
# a = "22"
# b = "213414"
# c = "32"
# print(a.rjust(8, "*"))
# print(b.rjust(8, "-"))
# print(c.rjust(8, "$"))
# print(a.ljust(8, "*"))
# print(b.ljust(8, "-"))
# print(c.ljust(8, "$"))

s = "Карпов Андрей Сергеевич"
name, surname, second_name = s.split()
print(name, surname, second_name)

nums = "1, 23   , 211 , 23,   21"
print(nums.replace(" ", "").split(","))
words = ['str', 'float', 'bool']
print(",".join(words))
print(words)
#
a = "  Аааааааааа   "
print(a.strip())
print(a.rstrip())
print(a.lstrip())