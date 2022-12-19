def exercise1(first_number, second_number, operator):
    print("*" * 10, "ex1", "*" * 10)
    if operator == "+":
        print(f"{first_number + second_number}")
    elif operator == "-":
        print(f"{first_number - second_number}")
    elif operator == "*":
        print(f"{first_number * second_number}")
    elif operator == "/":
        print(f"{first_number / second_number}")
    elif operator == "**":
        print(f"{first_number ** second_number}")


def exercise2(number):
    print("*" * 10, "ex2", "*" * 10)
    output = []
    i = 1
    while i ** 2 <= number:
        a = i ** 2
        output.append(a)
        i += 1
    print(*output)


def exercise3(number):
    print("*" * 10, "ex3", "*" * 10)
    if number > 2:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    else:
        return False


def exercise4(number):
    if number >= 0:
        if number == 0:
            print(f'Маша не нашла в лесу грибов')
        elif 10 <= number%100 <= 20:
            print(f'Маша нашла в лесу {number} грибов')
        elif number%10==1:
            print(f'Маша нашла в лесу {number} гриб')
        elif 2 <= number%10 <= 4:
            print(f'Маша нашла в лесу {number} гриба')
        else:
            print(f'Маша нашла в лесу {number} грибов')
    else:
        print(f'Маша потеряла в лесу грибы')


def main():
    exercise = int(input('Please eneter number of exercise (1-4): '))
    if exercise > 4 or 1 > exercise:
        print("No such answer! Please enter number of exercise (1-4)")
    elif exercise == 1:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        operator = input("Enter operator(=,-,/,*,**): ")
        exercise1(first_number, second_number, operator)
    elif exercise == 2:
        number = int(input('Enter number: '))
        exercise2(number)
    elif exercise == 3:
        number = int(input('Enter number: '))
        if exercise3(number):
            print("Simple")
        else:
            print("Not simple")
    elif exercise == 4:
        number = int(input('Enter grib: '))
        exercise4(number)


main()
