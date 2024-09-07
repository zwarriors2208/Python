a=float(input("Enter 1st no:"))
c=input("Enter the operator:")
b=float(input("Enter 2nd no:"))

if c=="+":
    print("The sum is :",a+b)
elif c=="-":
    print("The difference is :",a-b)
elif c=="*":
    print("The product is :",a*b)
elif c=="/":
    print("The quotient is :",a/b)
else:
    print("Invalid operator")


