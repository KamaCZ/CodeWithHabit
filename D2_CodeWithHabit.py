# Calculator
"""
Assignment:
The user of the calculator will write two numbers and an operator and the program
will make the calculation with these two numbers depanding on the type of operator
Procedure:
1) creating two variables for numbers and one variable for the operator
2) we will be using if, elif, and else statement to say the program what to do 
depanding on the the of the operator stored into the variable
"""

num1 = float(input("Enter the first number: "))
op = input("Enter the operator(+,-,*,/): ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("You did not enter numbers or a valid operator.")