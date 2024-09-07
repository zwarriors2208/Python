
while(True):
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
    s=input("Do you want to stop? Press 'n' if you want to exit")
    if s.lower()=="n":
        break

