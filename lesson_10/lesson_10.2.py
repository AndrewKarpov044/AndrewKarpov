# set_1 = {x ** 2 for x in range(1,5)}
# print(set_1)

# lst_1 = [1, 2, 3, 4 , 5, -3, 21, "21", "4"]
# # set_2 = {int(x) for x in lst_1 }
# set_2 = {int(x) for x in lst_1 if int(x) > 5}
# print(set_2)

# dict_1 = {x: x ** 2 for x in range(1, 5)}
# print(dict_1)

dict_2 = {"Russia": "moscow", "Russian": "saint Peter's"}
dict_3 = {key.upper(): val.capitalize() for key, val in dict_2.items()}
print(dict_2)
print(dict_3)
