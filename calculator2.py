def add(*numbers):
    return sum(numbers)

def subtract(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Cannot divide by zero"
        result /= num
    return result

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ["add", "subtract", "multiply", "divide"]:
        num_str = input("Enter numbers separated by spaces: ")
        num_list = [float(x) for x in num_str.split()]

        if user_input == "add":
            print("Result:", add(*num_list))
        elif user_input == "subtract":
            print("Result:", subtract(*num_list))
        elif user_input == "multiply":
            print("Result:", multiply(*num_list))
        elif user_input == "divide":
            print("Result:", divide(*num_list))
        else:
            print("Invalid input")
    else:
        print("Invalid input")
