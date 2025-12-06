numbers = [12, 5, 7, 3, 19, 3]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second smallest number is:", unique_numbers[1])
else:
    print("List does not have a second smallest number.")
