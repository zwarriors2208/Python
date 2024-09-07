acc_bal=float(input("Enter your account balance:"))
while(True):
    with_amt=float(input("Enter your withdrawal amount in multiples of 10:"))
    if(with_amt>acc_bal):
        print("Insufficient balance")
    elif with_amt % 10 != 0:
        print("withdrawal amount must be multiple of 10")
    else:
        print("Remaining balance is", acc_bal - with_amt)
        a = input("Do you want to withdraw more money(y/n): ")
        if(a.upper() == 'N'):
            break
        elif a.upper() == 'Y':
            continue
        else:
            print("Invalid input")
            break