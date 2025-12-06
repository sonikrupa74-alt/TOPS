p = float(input("Enter principal Amount : "))
r = float(input("Enter Rate of Interest (%) : "))
t = float(input("Enter Time (in years) : "))
n = int(input("Enter number of times interst is counpounded per year : "))

A = p * (1 + r/n) ** (n*t)
CI = A - p

print("Compound Interest : ",CI)
print("Total amount : ",A)
