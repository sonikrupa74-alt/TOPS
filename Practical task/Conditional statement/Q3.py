a,b,c = map(int,input("Enter three numbers : ").split())
if a>b and a > c:
    print("A is greatest")
elif b>a and b>c:
    print("B is greatest")
else:
    print("C is greatest")