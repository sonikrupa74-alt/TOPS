phy = int(input("Input marks obtained in Physics: "))
chem = int(input("Input marks obtained in Chemistry: "))
math = int(input("Input marks obtained in Mathematics: "))

total = phy + chem + math
totalMP = math + phy

if (math >= 65 and phy >= 55 and chem >= 50 and total >= 190) or (totalMP >= 140):
    print("The candidate is eligible.")
else:
    print("The candidate is not eligible.")
