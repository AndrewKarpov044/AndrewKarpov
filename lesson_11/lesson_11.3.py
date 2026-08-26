# def add_str(*args):
#     return " ".join(args)
# print(add_str("1dasdas", "2sfdsfdfd", "3dfdfdf"))

def add_str(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    if kwargs.get("sep"):
        sep = kwargs["sep"]
    return sep.join(args)

add_str("1dasdas", "2sfdsfdfd", "3dfdfdf", sep = "-", upper = True)