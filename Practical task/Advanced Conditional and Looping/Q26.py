n = int(input("Enter a number: "))
num = n

if num < 1:
    print(False)
else:
    while num % 2 == 0:
        num //= 2
    print(num == 1)
