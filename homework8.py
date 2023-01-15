
def ex_1(my_list: list) -> list:
    """
    :param my_list:
    :return: new_list_1
    """
    new_list_1 = my_list.copy()
    for i in range(1,len(new_list_1),2):
        new_list_1[i] = new_list_1[i][::-1]
    print(new_list_1)
    return new_list_1


def ex_2(my_list: list) -> list:
    """
    :param my_list:
    :return: new_list_2
     """
    new_list2 = [i for i in my_list if i[0] == 'a']
    print(new_list2)
    return new_list2

def ex_3(my_list: list) -> list:
    """
    :param my_list:
    :return: new_list_3
    """
    new_list3 = [i for i in my_list if 'a' in i]
    print(new_list3)
    return new_list3


def ex_4(my_list: list) -> list:
    """
    :param my_list:
    :return: new_list_4
    """
    new_list4 = [i for i in my_list if type(i) == str]
    print(new_list4)
    return new_list4


def ex_5(my_str: str) -> list:
    """
    :param my_str:
    :return: new_list_5
    """
    new_list5 = [i for i in my_str if my_str.count(i) == 1]
    print(new_list5)
    return new_list5

def ex_6(my_str: str, my_str_2: str) -> list:
    """
    :param my_str:
    :param my_str_2:
    :return: new_list_6
    """
    new_list6 = [i for i in set(my_str + my_str_2) if i in my_str and i in my_str_2]
    print(new_list6)
    return new_list6

def ex_7(my_str: str, my_str_2: str) -> list:
    """
    :param my_str:
    :param my_str_2:
    :return: new_list_7
    """
    new_list7 = [i for i in (my_str+my_str_2) if (my_str + my_str_2).count(i) == 1]
    print(new_list7)
    return new_list7
