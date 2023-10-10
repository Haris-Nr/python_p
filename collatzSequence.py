def collatz(number):
    try:
        while number != 1:
            number = int(input("Enter your number: "))
            if number <= 0:
                print("please enter positive integer")
                continue
            if number % 2 == 0:
                number //= 2
                print(number)
            elif number % 2 == 1:
                number = 3 * number + 1
                print(number)
        return number   
    except ValueError:
        print("Please enter a valid integer")



num = int(input("Enter your number: "))
print(collatz(num))