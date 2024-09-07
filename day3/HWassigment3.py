##program to manage a book collection using dictionaries

#d is global dictionary in which data of book will be stored
d = {}


def main():
    add_book()
    # ip = input(
            # "\n-->press 1 if you want to add more books\n-->press 2 if you want to search books\n-->press 4 if you want to remove a book\n-->Enter one of the following option[1,2,3]: ")
    while True:
        ip = input(
            "\n-->press 1 if you want to add more books\n-->press 2 if you want to search books\n-->press 3 if you want to remove a book\n-->Enter one of the following option[1,2,3]: ")
        if ip == "1":
            add_book()
        elif ip == "2":
            a1 = input("Enter the name of author or genre you want to search: ")
            search(a1)
        else:
            break

    print(d)

def add_book():
    name = input("Enter the name of BOOK you want to add: ")
    aut = input("Enter the name of author of the book: ")
    genre = input("Enter the name of genre of the book: ")
    year = input("Enter the year of publication of the book: ")
    d[name] = {'author' : aut, 'genre' : genre, 'year' : year}




def search(s):
    for books in d.keys():
        temp = d[books]
        if temp['author'] == s or temp['genre'] == s:
            print("the name of book is :", books , "\nthe details of book are :", temp)
            break
        else:
            continue

if __name__ == "__main__":
    main()
