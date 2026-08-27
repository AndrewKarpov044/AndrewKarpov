#Задание1
print("Декораторы в Python\nЗадание1")
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())

#Задание2
print("Задание 2")
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range (n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")
hello()