def exercise1():
    my_string = "0123456789"
    for i in my_string:
        for j in my_string:
            print(int(i+j), end=" ")


def exercise2():
    n = int(input("высота: "))
    for i in range(1, n + 1):
        for j in range(n - i):
            print(' ', end=' ')
        for z in range(2 * i - 1):
            if z == 0 or z == 2 * i - 2:
                print('*', end=' ')
            else:
                if i == n:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
        print()

def exercise3():
    n = int(input("высота: "))
    for i in range(n):
        for j in range(n-i):
            print(' ', end=' ')
        for j in range(2*i+1):
            if j==0:
                print('*',end=' ')
            elif j==2*i:
                print('*', end=' ')
            elif i == n-1:
                print('*', end=' ')
            else:
                print('*', end=' ')
        print()


def exercise4():
    n = int(input("высота: "))
    for i in range(1, n + 1) :
        for j in range(1, n - i + 1):
            print(end=' ')
        for l in range(1, 2 * i):
            if l == 1 or l == i * 2 - 1:
                print('*', end="")
            else:
                print('*', end="")
        print()
    for i in range (n - 1, 0, -1) :
        for j in range(1, n - i + 1):
            print(' ', end='')
        for l in range(1, 2 * i):
            if l == 1 or l == i * 2 - 1:
                print('*', end='')
            else:
                print(' ', end="")
        print()

def exercise5():
    n = int(input("высота: "))
    for i in range(1, n + 1):
        for j in range(n * 2 - i * 2):
            print(' ', end='')
        for z in range(2 * i - 1):
            print('*', end=' ')
        print()
    for i in range(n - 1):
        for j in range(i + 1):
            print(' ', end=' ')
        for j in range(2 * (n - i - 1) - 1):
            if j == 0 or j == 2 * (n - i - 1) - 2 or j == (n - i - 1) - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


def main():
    exercise = int(input("Enter exercise (1-2): "))
    if exercise == 1:
        print("*" * 10, "ex1", "*" * 10)
        exercise1()
    if exercise == 2:
        print("*" * 10, "ex2", "*" * 10)
        exercise2()
        exercise3()
        exercise4()
        exercise5()
    if 1 < exercise > 2:
        print("No such answer! Please eneter (1-3)")
main()






