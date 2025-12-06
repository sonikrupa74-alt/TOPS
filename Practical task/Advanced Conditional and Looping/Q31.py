num = input("Enter a number: ")
rev = ""

for ch in num:
    rev = ch + rev

if num == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
