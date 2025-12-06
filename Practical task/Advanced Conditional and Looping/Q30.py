n = int(input("Enter n: "))

total = 0
i = 1
count = 0

while count < n:
    total += i
    i += 2
    count += 1

print("Sum of first", n, "odd numbers:", total)
