#Safe Calculator

#Requirements:
#Support the four basic operations: addition, subtraction, multiplication, and division
#The program must not crash if the user enters 0 as the divisor
#The program must not crash if the user enters something that is not a number
#The program should exit gracefully when the user types quit

print("Welcome to my Calculator App!")
print("Type 'quit' to exit the app anytime.")

while True:
    first_input = input("\nPlease enter the first number: ")
    if first_input.lower() == "quit":
        print("Goodbye!")
        break

    second_input = input("Please enter the second number: ")
    if second_input.lower() == "quit":
        print("Goodbye!")
        break

    operation = input("Choose an operation (+, -, *, /): ")
    if operation.lower() == "quit":
        print("Goodbye!")
        break

    try:
        first_number = float(first_input)
        second_number = float(second_input)

        if operation == "+":
            result = first_number + second_number
            print("Result:", result)
        elif operation == "-":
            result = first_number - second_number
            print("Result:", result)
        elif operation == "*":
            result = first_number * second_number
            print("Result:", result)
        elif operation == "/":
            if second_number == 0:
                print("Second number cannot be zero for division. Please try again.")
            if first_number == 0:
                print("First number cannot be zero for division. Please try again.")
            else:
                result = first_number / second_number
                print("Result:", result)
        else:
            print("Invalid operation. Please choose from +, -, *, /.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("\nThank you for using the Calculator App. Goodbye!")