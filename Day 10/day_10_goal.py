# ===========================================================================================
# Calculator
# ===========================================================================================
# Script-purpose : This script implements an interactive calculator that performs addition,
# subtraction, multiplication, and division. It allows the user to continue
# calculating with the current result or start a new calculation, creating a
# smooth loop-based workflow for repeated operations.
# ===========================================================================================

import os
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return float(n1) * float(n2)

def divide(n1, n2):
    return float(n1) / float(n2)

def clear_screen():
    os.system('cls')

def perform_calculation():
    print(art.logo)
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    should_continue = True
    num1 = float(input("What is the first number ? : "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What is the second number ? : "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if user_choice == 'y':
            num1 = answer
        else:
            print("\n" * 20)
            perform_calculation()

perform_calculation()
