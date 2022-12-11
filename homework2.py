exercise = int(input("Enter exercise (1-3): "))
if exercise == 1:
    print("*"*10,"ex1","*"*10)
    n = int(input("Enter a children: "))
    k = int(input("Enter an apples "))
    apples_in_children = k//n
    print(f'Apples for every student: {apples_in_children}')
    print(f"Apples left in the basket: {k-(k//n)*n}")
if exercise == 2:
    print("*"*10,"ex2","*"*10)
    class1= int(input("Enter desks in class1: "))
    class2 = int(input("Enter desks in class2: "))
    class3 = int(input("Enter desks in class3: "))
    print(f"Parts need to buy: {(class1 // 2 + class1 % 2)+(class2 // 2 + class2 % 2)+(class3 // 2 + class3 % 2)}")
if exercise == 3:
    print("*"*10,"ex3","*"*10)
    numbers = int(input())
    print(int(f"{numbers % 10}{(numbers % 100) // 10}{numbers // 100}"))
if 1 < exercise > 3:
    print("No such answer! Please eneter (1-3)")
