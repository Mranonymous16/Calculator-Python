import time

def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

def exp(num1,num2):
    return num1 ** num2

ans = 'y'
while(ans=='y'):
    print("Please select operation -\n"
            "1. Add\n"
            "2. Subtract\n"
            "3. Multiply\n"
            "4. Divide\n"
            "5. exponential\n")

    select = int(input("Select operation: "))

    if select == 1:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "+", number_2, "=", add(number_1, number_2))
        time.sleep(2)

    elif select == 2:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "-", number_2, "=", subtract(number_1, number_2))
        time.sleep(2)

    elif select == 3:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
        time.sleep(2)

    elif select == 4:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "/", number_2, "=", divide(number_1, number_2))
        time.sleep(2)

    elif select == 5:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: "))
        print(number_1, "^", number_2, "=", exp(number_1, number_2))
        time.sleep(2)

    else:
        print("Invalid Option!! Please Select Valid Option")
        time.sleep(2)

    ans = input("press 'y' to continue: ")