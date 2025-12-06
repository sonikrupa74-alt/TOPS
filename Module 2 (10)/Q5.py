text = input("Enter name : ")
if len(text) < 3:
    result = text
elif text.endswith("ing"):
    result = text+"ly"
else:
    result = text + "ing"

print("Result : ",result)