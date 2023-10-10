
        

def calculator():
    # This calculator can calculate sum(any operation) of any two numbers
    print("This calculator can calculate floats also.")
    # Taking data from user
    first_number = float(input("Enter first number: "))
    operation = input("Enter operation: ")
    second_number: float = float(input("Enter second number: "))
    # Performing calculations and printing the results in readable form
    while True:
        if operation == "+":
            sum1 = first_number + second_number
            print("The answer is ", sum1)
            answ = input("Do you want to use calculator again.If yes write 'yes' if no write 'No':  ")
            answ.lower
            if answ == "no":
                print("Thank you for uinsg.......")
            else:
                calculator()
        elif operation == "-":
            sum1 = first_number - second_number
            print("The answer is ", sum1)
            break
        elif operation == "*":
            sum1 = first_number * second_number
            print("The answer is ", sum1)
            break
        elif operation == "/":
            sum1 = first_number / second_number
            print("The answer is ", sum1)
            break
        elif operation == "%":
            sum1 = first_number % second_number
            print("The answer is ", sum1)
            break
        elif operation == "//":
            sum1 = first_number // second_number
            print("The answer is ", sum1)
            break
        elif operation == "**":
            sum1 = first_number ** second_number
            print("The answer is ", sum1)
            break
        else:
            print("invalid operator.Please enter valid operator")

calculator()