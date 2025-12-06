text = input("Enter a string: ")
ch = input("Enter a character to count: ")

count = 0
for c in text:
    if c == ch:
        count += 1

print(f"Occurrences of '{ch}':", count)
