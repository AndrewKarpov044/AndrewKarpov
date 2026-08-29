# num: int = 0
#
# # num: float = 1.2
#
# def plus_2(a: int | float, b: int | float) -> int | float:
#     return a + b
#
# res = plus_2(4.2, 2)
#
# # print(plus_2(2, 3))
#
# print(res)
# print(plus_2.__annotations__)

# nums: list[int] = [1, 2, 5, 2, 1, 4, 2]
#
# nums.append("fdfqefe")
# print(nums)
#
# books = []
# book: tuple[str, str, int]
# book = ("Пушкин", "Золотая рыбка", 1900)
# books.append(book)
# book = ("Булгоков", "Мастер и Маргарита", "1900")
#
# capitals: dict[str, str] = {"Россия": "Москва"}
# capitals["Сша"] = "Вашингтон"

def list_upper_case(lst: list[int]) -> list[str]:
    return [x.upper() for x in lst ]

print(list_upper_case(["fwrewer", "fwrqwrewfd"]))