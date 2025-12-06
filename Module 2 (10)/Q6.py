text = input("Enter a string: ")

not_p = text.find("not")
poor_p = text.find("poor")

if not_p != -1 and poor_p != -1 and not_p < poor_p:
    text = text[:not_p] + "good" + text[poor_p+4:]

print("Result:", text)
