def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 + num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Invalid Division"


def choose_operation(number1, number2):
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
    op = input("Choose Operation: ")
    if op.isnumeric():
        op = int(op)
        if op > 4 or op < 1:
            print("Invalid Option")
            choose_operation(number1, number2)
        else:
            if op == 1:
                print("The Sum is: ", add(number1, number2))
            elif op == 2:
                print("The Difference is: ", subtract(number1, number2))
            elif op == 3:
                print("The Product is: ", multiply(number1, number2))
            elif op == 4:
                print("The Result is: ", divide(number1, number2))

    else:
        print("Invalid Option")
        choose_operation(number1, number2)


input_num1 = float(input("Enter First Number: "))
input_num2 = float(input("Enter Second Number: "))
choose_operation(input_num1, input_num2)
