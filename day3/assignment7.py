from sympy.codegen.ast import continue_

d={}
while True:
    ip=input("Enter the item name: ")
    i1 = int(input("Enter the quantity of item: "))
    i2 = float(input("Enter the price pf item: "))

    l=[i1,i2]
    d[ip]=l
    t=input("Do you want to add more items (Y/y):")
    if t.lower() == 'y':
        continue
    else:
        break
while True:
    print("\n\n")
    ip1 = input("do you want to update any of the existing item(yes/y):")
    if ip1.lower() == 'yes' or ip1.lower() == 'y':
        None
    else:
        break
    while True:
        ip3 = input("enter the name of item you want to update:")
        if ip3 in d.keys():
            break
        elif ip3.lower() == 'yes' or ip3.lower() == 'y':
            break
        else:
            print("There is no such item in your inventory): " )
            break
    i3 = int(input("Enter the quantity of item: "))
    i4 = float(input("Enter the price pf item: "))
    l2 = [i3,i4]
    d[ip3]=l2
print(d)
tot_l = 0
for value in d.values():
    tot_l += value[1]*value[0]

print("The total value of our inventory is :", tot_l)