"""
WAP to check if the given year is a leap year or not. 
"""

year = int(input("Enter a year : "))

if (year % 400 == 0) or (year % 4==0 and year % 1 != 0):
    print("it's a leap year !")
else:
    print("Not a leap year")

