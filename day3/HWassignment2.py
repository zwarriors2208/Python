#simple phonebook application using dictionaries

d = {}

def main():
    add_user()
    while True:
        ip = input(
            "\n-->press 1 if you want to add more user\n-->press 2 if you want to search user in phonebook\n-->press 3 if you want to update the user\n-->press 4 if you want to delete a user\n-->Enter one of the following option[1,2,3,4]: ")
        if ip == '1':
            add_user()
        elif ip == '2':
            a = input("enter the name of user you want to search: ")
            search(a)
        elif ip == '3':
            a1 = input("enter the name of user you want to update: ")
            if a1 in d.keys():
                a11 = input("enter the updated number of user: ")
                a22 = input("enter the updated mail of user: ")
                d[a1] = [a11, a22]
                print("Updation was success")
            else:
                print("user does not exist")
                continue
        elif ip == '4':
            a2 = input("enter the name of user you want to delete: ")
            del(d[a2])
            print("user deleted\n\n")
        else:
            break
    print(d)


def add_user():
    name = input("Enter the name of user you want to add: ")
    ph_no = input("Enter your phone number: ")
    email = input("Enter your email: ")
    l = [ph_no, email]
    d[name] = l
    return


def search(s):
    if s in d.keys():
        print("\nNumber and mail of", s, "is :", d[s])
    else:
        print("\nuser does not exist")


if __name__ == "__main__":
    main()