dict = {"Ramsaheb": "smart","Kunal":"dumb","mammi":"hoshiyar","papa":"hardworking"}
# print(dict["Ramsaheb"])

# for name in dict:
#     print(name)
#     print(name, dict[name])

# for key,val in dict.items():
#     print(key, val)

# dict["arbaz"] = "chutiya"
# print(dict)

# squared_num = {x: x**2 for x in range(10)}
# print(squared_num)

dict1 = ["Ramsaheb","Kunal","mammi","papa"]
default = "smart"
new_dict = dict.fromkeys(dict1, default)
print(new_dict)
