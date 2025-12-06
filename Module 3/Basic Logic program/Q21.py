"""
Accept 2 numbers from user and swap 2 numbers with using 3rd variable 
and without using 3rd variable
"""

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(f"Before swapping number 1 : {n1} and number 2 : {n2} ")
t1 = n1
n1 = n2
n2 = t1

print(f"After swapping number 1 : {n1} and number 2 : {n2}")

# without using third variable 
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n1 , n2 = n2 , n1
print(f"Without using third variable number 1 : {n1} and number 2 : {n2} ")