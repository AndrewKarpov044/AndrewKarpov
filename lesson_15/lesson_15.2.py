file_2 = "../requirements.txt"

try:
    f = open("file.txt")
    print("Файл открыт")
    try:
        text = f.read()
        print(text)
    finally:
        f.close()
        print("Файл закрыт")
except FileNotFoundError:
    print("Файл не найден")













