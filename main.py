def calculate(first_number, operand, second_number):
    if operand == "+":
        sum = int(first_number) + int(second_number)
        return sum
    elif operand == "-":
        sum = int(first_number) - int(second_number)
        return sum
    elif operand == "/":
        sum = int(first_number) / int(second_number)
        return sum
    elif operand == "*":
        sum = int(first_number) * int(second_number)
        return sum
    else:
        print("The operand you choosed is not compatible.")


if __name__ == "__main__":
    print("Python Calculator")

    first_number = input("Please enter your first number: ")
    operand = input("Choose you operand (+, -, /, *): ")
    second_number = input("Please enter your second number: ")

    result = calculate(first_number, operand, second_number)

    print("Your result is: " + str(result))