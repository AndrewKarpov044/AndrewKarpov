items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
# print(isinstance(items, list))
# print(isinstance(items, str))
result = [item for item in items if isinstance(item, (str, list))]
print(result)

def describe_type(x):
    if isinstance(x, str):
        print('Это строка')
    elif isinstance(x, int | float):
        print("Это число")
    elif isinstance(x, bool):
        print("Это булевое значене")
    else:
        print("Неизвестный тип")

describe_type("ffewrew")


