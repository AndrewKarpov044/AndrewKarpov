# name = "Andrew" #Глобальная переменная
#
# def func():
#     #Локальная переменная
#     name = "ANDREW"
#     print(name)
# func()
# #print(name)
# #print(name)
#
# """
# Очередность поиска переменной
# Local - Локальная переменная
# Global - Глобальная переменная
# # Builtin - Встроенные переменные (print, str и т.д.)
# """

# NAME = "Andrew"
def uppdate_name():
    NAME = "Andrew"
    def update_name2():
        nonlocal NAME
        NAME = "Sacha"
        print(NAME)
    update_name2()
    print(NAME)
uppdate_name()
print(NAME)