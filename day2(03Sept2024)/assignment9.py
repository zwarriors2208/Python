l = []

while True:
    ip = input("Enter one of the following operation you want to perform [add, remove, view or exit]:")
    match ip.lower():
        case 'add':
            i1 = input("Enter the name of task you want to add:")
            l.append(i1)
        case 'remove':
            i2 = input("Enter the name of task you want to remove:")
            l.remove(i2)
        case 'view':
            for i in range (len(l)):
                print(f"{i + 1} : {l[i]}")

        case 'exit':
            break
        case _:
            print("Invalid input")


