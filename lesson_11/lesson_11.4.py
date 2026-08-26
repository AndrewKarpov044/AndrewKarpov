# def example(*args):
#     a, *b= args
#     print(a, b)
# example(3, 56, 7, "sfd")
#
# def example(**kwargs):
#     print(kwargs)
# example(name = "Андрей", age = "23" )

dict_1 = dict(name = "Андрей", age = "23" )
print(dict_1)

def print_name_age(name, age):
    print(f"Мое имя - {name} - и мой возраст - {age}")
print_name_age(**dict_1)