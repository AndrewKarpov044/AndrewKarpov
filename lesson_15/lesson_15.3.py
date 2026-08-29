"""
w - write запись (очищает и перезаписывает)
a - append добавляет (Только добавляет)

w+ - запись и чтение(файл должен существовать)
a+ - добавление и чтение(можем читать и записывать в конце файла)
"""

# file_5 = "Снимок.PNG"
#
#
# with open (file_5, mode = "rb") as f:
#     image = f.read()
# # print(type(image))
#
# with open("Снимок2.png", mode = "wb") as f:
#     f.write(image)

# with open("out.txt", "w", encoding="utf-8") as f:
#     f.write("Текст 1\n")
#     f.write("Текст 3\n")
#
#
# with open("out.txt", "a", encoding="utf-8") as f:
#         f.write("Текст 2\n")
#
# lst = ["fdsfdf", "fdsfera"]
# lst_for_w = [text + "\n" for text in lst]
#
# with open("out.txt", "a", encoding="utf-8") as f:
#     f.writelines(lst_for_w)

with open("out.txt", "a+", encoding="utf-8") as f:
    print(f.tell())
    f.seek(0)
    f.write("Новая строка")
    f.seek(0)
    print(f.read())
    f.close()