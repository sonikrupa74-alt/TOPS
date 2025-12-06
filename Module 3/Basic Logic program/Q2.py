a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("choose operation :- ")
print("1. Addition")
print("2. Subtration")
print("3. Multiplication")
print("4. Division")

choice = input("\nEnter your choice (1/2/3/4) : ")

if choice == '1':
    print("Result : ",a+b )
elif choice == '2':
    print("Result : ",a-b)
elif choice == '3':
    print("Result : ",a*b)
elif choice == '4':
    if b!=0:
        print("Result : ",a/b)
    else:
        print("Zero is not allowed")
else:
    print("Invalid choice !")