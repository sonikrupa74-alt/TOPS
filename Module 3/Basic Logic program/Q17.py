salary = float(input("Enter your salary : "))

if salary <= 30000:
    premium = 0.05 * salary
elif salary <=50000:
    premium = 0.10 * salary
else:
    premium = 0.30 * salary

print("your insurance premium is : ",premium)