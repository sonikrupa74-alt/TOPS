str1 = "hello"
str2 = "guys"

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

result = new_str1 + " " + new_str2
print("Result : ",result) 