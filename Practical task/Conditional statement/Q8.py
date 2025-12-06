num = int(input("Enter number : "))

min = int(input("Enter minimum value : "))
max = int(input("Enter maximum value : "))

if min <= num <= max:
    print(f"The number is in range min:{min} max:{max}")
else:
    print("The number is not in range")