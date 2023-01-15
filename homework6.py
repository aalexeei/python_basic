from random import randint
my_list_1 = [randint(1, 100) for i in range(10)]
my_list_2 = [randint(80, 120) for i in range(10)]
print('Задание №3')
my_result = my_list_1[::2] + my_list_2[1::2]
print(f'my_result = {my_result}')
print()
print('Задание №11')
my_str_11 = '5gf5yh67hg'
print(my_str_11)
my_list = [i for i in my_str_11 if my_str_11.count(i) == 1]
print(my_list)