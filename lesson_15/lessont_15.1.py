file = "lesson_15.txt"
file_2 = "../requirements.txt"
# file_3 = "C:\PythonProject\PythonProject1\lesson_15\lesson_15.txt"
file_4 = "images.png"

"""
r - read чтение
w - write запись (очищает и перезаписывает)
a - append добавляет (Только добавляет)
x - create создаёт
r+ - чтение и запись(файл должен существовать)
w+ - запись и чтение(файл должен существовать)
a+ - добавление и чтение(можем читать и записывать в конце файла)
"""

f = open(file=file_2, encoding='utf-16')

text_2 = f.read()
print(text_2)

text_2_line = f.readline()
print(text_2_line)
print(type(text_2_line))

text_3_line = f.readlines()
print(text_3_line)
print(type(text_3_line))

# for line in f:
#     print(line, end="")
#
# print("Позиция до чтения", f.tell())
# text_2_line = f.readline()
# print("Позиция после чтения", f.tell())
# f.seek(0)
# print("Позиция после f.seek(0)", f.tell())
# f.seek(50)
# text_3 = f.read()
# print(text_3)
# text_3 = f.read(10)
# print(text_3)
# file_5 = "Снимок.PNG"
#
#
with open (file_5, mode = "rb") as f:
    image = f.read()
# print(type(image))

with open("Снимок2.png", mode = "wb") as f:
    f.write(image)






f.close()