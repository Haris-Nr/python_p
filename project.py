# import forex-python
from forex_python.converter import CurrencyRates
import time

def calculator():
    print("Welcome to the Calculator!")
    print("This calculator can calculate floats also.")
    
    while True:
        try:
            first_number = float(input("Enter the first number: "))
            operation = input("Enter the operation (+, -, *, /, %, //, **): ")
            second_number = float(input("Enter the second number: "))
            
            if operation == "+":
                result = first_number + second_number
            elif operation == "-":
                result = first_number - second_number
            elif operation == "*":
                result = first_number * second_number
            elif operation == "/":
                if second_number == 0:
                    print("Error: Division by zero")
                    continue
                result = first_number / second_number
            elif operation == "%":
                result = first_number % second_number
            elif operation == "//":
                result = first_number // second_number
            elif operation == "**":
                result = first_number ** second_number
            else:
                print("Invalid operator. Please enter a valid operator.")
                continue

            print("The answer is", result)

            # Currency exchange
            currency_exchange = input("Do you want to perform currency exchange (yes/no): ").lower()
            if currency_exchange == "yes":
                currency_from = input("Enter the currency you want to convert from (e.g., USD): ").upper()
                currency_to = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
                amount = float(input(f"Enter the amount in {currency_from}: "))

                c = CurrencyRates()
                converted_amount = c.convert(currency_from, currency_to, amount)
                print(f"{amount} {currency_from} is equal to {converted_amount} {currency_to}")

            # Alarm clock
            alarm_option = input("Do you want to set an alarm (yes/no): ").lower()
            if alarm_option == "yes":
                alarm_time = input("Enter the time for the alarm in HH:MM format: ")
                current_time = time.strftime("%H:%M")
                while current_time != alarm_time:
                    current_time = time.strftime("%H:%M")
                    time.sleep(1)
                print("Alarm! Time to wake up!")

            continue_calculations = input("Do you want to use the calculator again (yes/no): ").lower()
            if continue_calculations != "yes":
                print("Thank you for using the calculator!")
                break

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    calculator()
