""" Accept monthly salary from the user and deduct 10% insurance premium, 
10% loan installment find out of remaining salary. """

salary = float(input("Enter monthly salary : "))

insurance = salary * 0.10
loan = salary * 0.10

remaining_salary = salary - (insurance + loan)

print("Insurance deduction : ",insurance)
print("Loan deuction : ",loan)
print("Remaining salary : ",remaining_salary)