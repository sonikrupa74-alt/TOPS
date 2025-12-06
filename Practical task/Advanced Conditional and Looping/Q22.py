n = int(input("Enter a number: "))
total = 0
num = n

while num > 0:
    total += num % 10
    num //= 10

print("Sum of digits:", total)
