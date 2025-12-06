lst = list(map(int, input("Enter numbers separated by space: ").split()))
unique = []

for num in lst:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)
