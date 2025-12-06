string = input("Enter a string: ")
no_space = ""
for ch in string:
    if ch != " ":
        no_space += ch
print("String without spaces:", no_space)
