HISTORY_FILE = "history.txt"

def show_history():
    with open(HISTORY_FILE, 'r') as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("No history found.")
        else:
            for line in reversed(lines):
                print(line.strip())
    file.close()


def clear_history():
    with open(HISTORY_FILE, 'w') as file:
        file.write("")
        print("History cleared successfully.")
    file.close()


def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")
    file.close()



def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. Please use: <number1> <operator> <number2>")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Division by zero is not allowed.")
            return
        result = num1 / num2
    elif op == '%':
        result = num1 % num2 
    else:
        print("Unsupported operator. Please use +, -, *, / or %.")
        return
    
    if int(result) == result:
        result = int(result)

    print(f"Result: {result}")
    save_to_history(user_input, result)


def main():
    print("-----SIMPLE CALCULATOR-----")
    try:
        while True:
            user_input = input("Enter calculation(+ - * /) or command('history', 'clear', 'exit'): ").strip().lower()
            if user_input == 'exit' or user_input == 'e':
                print("Exiting the calculator. Goodbye!")
                break
            elif user_input == 'history' or user_input == 'h':
                show_history()
            elif user_input == 'clear' or user_input == 'c':
                clear_history()
            else:
                calculate(user_input)
    except Exception as err:
        print(f"An error occurred: {err}")


main()