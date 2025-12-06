string = input("Enter a string: ")
substring = input("Enter substring: ")
positions = []
start = 0

while True:
    index = string.find(substring, start)
    if index == -1:
        break
    positions.append(index)
    start = index + 1

print(positions)
