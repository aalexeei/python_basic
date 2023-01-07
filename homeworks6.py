def exercise1():
    my_list1 = [1,2,3,4]
    my_list2 = [5,6,7,8]
    my_result = my_list1[1::2]+my_list2[::2]
    print(my_result)
exercise1()
def exercise2():
    my_str= "1,2,3,4,4,3,2"
    my_result = []
    [my_result.append(i) for i in my_str if my_str.count(i) == 1]
    print(my_result)
exercise2()