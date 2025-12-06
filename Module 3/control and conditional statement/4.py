""""
WAP to make simple calculator (operation include Addition, Subtraction, 
Multiplication, Division, modulo) using conditional statement  
"""

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

operation = input("Enter operation : ")

if operation  == "+":
    print("Addition : " ,a+b)

elif operation == "-":
    print("Subtraction : ",a-b)

elif operation == "*":
    print("Multplication : ",a*b)

elif operation == "/":
    print("Division : ",a/b)