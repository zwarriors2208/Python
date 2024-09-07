a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
o=input("Enter operator: ")

match o:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("Invalid Operator")
