n = int(input("Enter n: "))
fib_list = []

a, b = 0, 1
count = 0

while count < n:
    fib_list.append(a)
    a, b = b, a + b
    count += 1

print(fib_list)
