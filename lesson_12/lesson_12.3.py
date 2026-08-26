def say_name(name):
    def say_goodbye():
        print(f"Пока {name}")
    return say_goodbye

say_andrew = say_name("Andrew")
say_igor = say_name("Igor")

say_andrew()
say_igor()

def printsaq():
    print(1243)
print(say_andrew.__closure__)
print(printsaq.__closure__)