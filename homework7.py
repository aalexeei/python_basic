
print("############# ex1")

person = [{"name": "John",
           "age": 55},
           {"name": "Jackson",
            "age": 8},
          {"name": "Jacksin",
           "age": 8}]

names_list = []
names_ages = [(i["name"], i["age"]) for i in person]
ages = sorted(names_ages, key=lambda x: x[1])
min_age = ages[0]
for name, age in ages:
    if age == min_age[1]:
        names_list.append(name)
    else:
        break
print("Задание а:",names_list)


names_list = []
names = [i["name"] for i in person]
name_sort = sorted(names, key=lambda x: x[1])       #### add  ,reverse=True for min name
max_name = name_sort[0]
for i in name_sort:
    if len(i) == len(max_name):
        names_list.append(i)
    else:
        break
print("Задание б:",names_list)

print("Задание в:", sum([i["age"] for i in person])/len(person))

print("############# ex2")
my_dict_1 = {"name": "John", "surname": 'lolik', "car": 'audi'}
my_dict_2 = {"name": "John2", "age": 55}


list_a =[]
list_b = []
for i in my_dict_1.keys():
    if i in my_dict_2:
        list_a.append(i)
    if not i in my_dict_2:
        list_b.append(i)
print(f"Задание а: {list_a}")
print(f"Задание б: {list_b}")

list1 = []
list2 = []
for i in list_b:
    list1.append(i)
    list2.append(my_dict_1.get(i))
my_dict_3 = dict(zip(list1,list2))
print(f"Задание в: {my_dict_3}")

my_dict_4 = {}
for i in my_dict_1:
    if i in my_dict_2:
        my_dict_4.update([(i, [my_dict_1[i], my_dict_2[i]])])
    else:
        my_dict_4.update([(i, my_dict_1[i])])
for j in my_dict_2:
    if j not in my_dict_1:
        my_dict_4.update([(j, my_dict_2[j])])
print(f"Задание г: {my_dict_4}")

