CLI Calculator (Python)
## Overview

This is a simple Command-Line Interface (CLI) Calculator built using Python.
It allows users to perform basic arithmetic operations such as Addition, Subtraction, Multiplication, and Division directly from the terminal.
The program runs continuously until the user chooses to exit.

## Features

Supports basic operations: Addition, Subtraction, Multiplication, Division
Handles division by zero gracefully
Accepts only integer operands
Provides a user-friendly CLI menu
Runs in a continuous loop until exited by the user

## How It Works

1. The program displays a list of available operations.

2. The user selects an operation by entering a number (1–5).

3. The calculator prompts for two operands (integers).

4. The selected operation is performed and the result is displayed.

5. The loop continues until the user selects option 5 to exit.

Example Run
The operations you can perform are :
1: Addition
2: Subtraction
3: Multiplication
4: Division
5: Exit
operands must be integers

Enter the number of the operation you want to perform : 1
Enter the first operand: 10
Enter the second operand: 5
answer is: 15

## Concepts Used

Classes and Objects
Methods
Conditional Statements
Loops
Exception Handling (ZeroDivisionError)

## How to Run

Save the code in a file named calculator.py.
Open your terminal or command prompt.
Navigate to the directory containing calculator.py.
Run the program using:
python calculator.py

## Notes

Only integer inputs are supported in this version.
Enter 5 to exit the calculator safely.