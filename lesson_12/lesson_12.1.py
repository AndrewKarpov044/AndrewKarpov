mult = lambda a, b: a * b
print(mult(2,3))

lst_1 = ["Красноярск", "Курск", "Елец"]

# def len_word(word):
#     return len(word)

# print(len_word(lst_1))
sorted_lst = sorted(lst_1, key =lambda word: len(word))
print(sorted_lst)

func = lambda word: len(word)