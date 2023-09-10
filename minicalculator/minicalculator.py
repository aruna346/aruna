# Initialize a list to store calculation history
history = []

# Define a function for addition
def addition(num1, num2):
    result = num1 + num2
    # Append the calculation history to the list
    history.append(f"Addition: {num1} + {num2} = {result}")
    return result

# Define a function for subtraction
def subtraction(num1, num2):
    result = num1 - num2
    # Append the calculation history to the list
    history.append(f"Subtraction: {num1} - {num2} = {result}")
    return result

# Define a function for division
def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    result = num1 / num2
    # Append the calculation history to the list
    history.append(f"Division: {num1} / {num2} = {result}")
    return result

# Define a function for multiplication
def multiplication(num1, num2):
    result = num1 * num2
    # Append the calculation history to the list
    history.append(f"Multiplication: {num1} * {num2} = {result}")
    return result

# Define a function to save history to a file
def save_history():
    with open("calculation_history.txt", "a") as file:
        for item in history:
            file.write(item + "\n")

# Define a function to load history from a file
def load_history():
    try:
        with open("calculation_history.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

# Load calculation history from the file (if it exists)
history = load_history()

# Main program loop
while True:
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Show History")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '6':
        save_history()  # Save history to the file before quitting
        print("Goodbye!")
        break
    elif choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = addition(num1, num2)
        elif choice == '2':
            result = subtraction(num1, num2)
        elif choice == '3':
            result = division(num1, num2)
        elif choice == '4':
            result = multiplication(num1, num2)

        print(f"Result: {result}")
    elif choice == '5':
        print("Calculation History:")
        for item in history:
            print(item)
    else:
        print("Invalid input. Please select a valid option.")
