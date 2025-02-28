# --------------------- Project ------------------------------
# The Calculator Project
# ------------------------------------------------------------

# --------------------- Objectives ---------------------------
# Understanding function with outputs & multiple return values
# ------------------------------------------------------------

from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

symbols = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    should_continue = True

    num1 = float(input("What's the first number? : "))

    while should_continue:

        print("\n")
        for key in symbols:
            print(key)

        operation = input("Pick an operation : ")
        num2 = float(input("\nWhat's the next number ? : "))

        result = symbols[operation](num1, num2)

        print(f"\n{num1} {operation} {num2} = {result}")

        print("\n----------------------------------------------------------------------------------------------")
        choice = input(f"Type 'y' to continue calculating with {result},"
                       f"\n\tor type 'n' to start a new calculation : ")

        if choice == 'y':
            num1 = result
        elif choice == 'n':
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()