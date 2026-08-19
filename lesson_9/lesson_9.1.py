# dict_ex = ["Андрей", "Карпов", "23", ["Москва", "Павлово", "Нижний"]]
# dict_ex = { "name": "Andrew", "last_name": "Karpov", "age": 23, "age": 24, "cities": ["Москва", "Павлово", "Нижний"], "smole": False}
#
# print(dict_ex["age"])
#
# dict_ex = dict(name = "Andrew", last_name = "Karpov")
# print(dict_ex)
#
# dict_ex = [["name", "Andrew"], ["last_name", "Karpov"]]
# print(dict_ex)
#
# dict_ex = dict(dict_ex)
# print(dict_ex)
#
# """
# Ключами могут быть
# str
# int
# bool
# tuple
# """
# # del dict_ex["age"]
# print(len(dict_ex))
# print(dict_ex)
# print("name" in dict_ex)
#
# dict_ex = dict.fromkeys(["Andrew", "Karpov", "23"], "data")
# dict_ex.clear()
# print(dict_ex)
#
# # dict_ex2 = dict_ex.copy()
# dict_ex2 = dict(dict_ex)
# dict_ex2["age"] = 25
# dict_ex2["age2"] = 30
# print(id(dict_ex))
# print(dict_ex)
# print(id(dict_ex2))
# print(dict_ex2)
#
# name = dict_ex.get("fdsfdsf")
# if name:
#     print(name)
# #
# dict_ex.setdefault( "namfsdfae", "Andrew")
# dict_ex.setdefault( "agfdfasdfe", 23)
# print(dict_ex)
# print(dict_ex)
# str_1 = dict_ex.pop("fdfds", "key none")
# print(str_1)
#
# # print(dict_ex)
# print(dict_ex)
# str_1 = dict_ex.popitem()
# print(str_1)
# print(dict_ex)
#
# print(list(dict_ex.keys()))
# print(list(dict_ex.values()))
# print(list(dict_ex.items()))
#
# for key, value in dict_ex.items():
#     print(key, value)
#
dict_ex1 = { "name": "Andrew"}
dict_ex2 = {"last_name": "Karpov"}
dict_ex1.update(dict_ex2)

print(dict_ex1)
print(dict_ex2)

# dict_res = {** dict_ex1, ** dict_ex2}
# print(dict_res)