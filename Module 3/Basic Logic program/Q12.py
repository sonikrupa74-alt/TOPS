students = int(input("Enter a number of students : "))
if students < 0:
    print("number of students can't be negative")
else:
    apples = 5 * students
    print("Apples required : ",apples)