week = int(input("Enter week number (1-7): "))

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 1 <= week <= 7:
    print("Day is", days[week-1])
else:
    print("Invalid week number")
