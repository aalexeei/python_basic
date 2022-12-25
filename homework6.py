import random


def random_list():
    randomlist = []
    for i in range(0, 5):
        n = random.randint(80, 200)
        randomlist.append(n)
    return randomlist


def exercise1():
    randomlist = random_list()
    print(randomlist)
    for i in range(len(randomlist)):
        if randomlist[i] > 100:
            print(randomlist[i],end=" ")


def exercise2():
    randomlist = random_list()
    print(randomlist)
    my_result = []
    for i in range(len(randomlist)):
        if randomlist[i] > 100:
            my_result.append(randomlist[i])
    print(my_result)


def exercise3():
    randomlist = random_list()
    print(randomlist)
    if len(randomlist) < 2:
        randomlist.append(0)
    else:
        randomlist.append(randomlist[-1] + randomlist[-2])
    print(randomlist)


def exercise4():
    randomlist = random_list()
    print(randomlist)
    k = int(input("индекс элемента: "))
    for i in range(k, len(randomlist) - 1):
        randomlist[i] = randomlist[i + 1]
    randomlist.pop(len(randomlist) - 1)
    for i in range(len(randomlist)):
        print(randomlist[i], end=' ')


def exercise5():
    randomlist = random_list()
    print(randomlist)
    k = int(input('Введите k '))
    с = int(input('Введите с '))
    randomlist = randomlist[:k] + [с] + randomlist[k:]
    print(randomlist)


def exercise6():
    list1 = [1, 2, 4, 5, 6, 99, 8]
    list2 = [6, 7, 8, 9, 33, 45, 66]
    print(f"Уникальных чисел: {len(set(list1) & set(list2))}")

def main():
    exercise = int(input("Enter exercise (1-6): "))
    if exercise == 1:
        print("*" * 10, "ex1", "*" * 10)
        exercise1()
    if exercise == 2:
        print("*" * 10, "ex2", "*" * 10)
        exercise2()
    if exercise == 3:
        print("*" * 10, "ex3", "*" * 10)
        exercise3()
    if exercise == 4:
        print("*" * 10, "ex4", "*" * 10)
        exercise4()
    if exercise == 5:
        print("*" * 10, "ex5", "*" * 10)
        exercise5()
    if exercise == 6:
        print("*" * 10, "ex6", "*" * 10)
        exercise6()
    if 1 < exercise > 6:
        print("No such answer! Please eneter (1-3)")
main()