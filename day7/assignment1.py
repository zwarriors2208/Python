class Book:
    title = ''
    author = ''
    year = 2000
    available = False
    def __init__(self, title234, author, year, available):
        self.title = title234
        self.author = author
        self.year = year
        self.available = available
    def display_details(self):
        print(f"Title: {self.title} \nWritten By: {self.author} \nYear: {self.year}")
        if self.available:
            print(f"Available: Yes\n")
        else:
            print(f"Available: No\n")

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"The book has been borrowed")
        else:
            print(f"The book is already borrowed by someone else")

    def return_book(self):
        self.available = True
        print(f"The book has been returned")

book1 = Book("Atomic Habits", "Ankit Kumar", 2020, 1)
book2 = Book("Harri putter", "AAryan Pal", 2024, 1)
book1.display_details()
book2.display_details()
book1.borrow_book()
book1.borrow_book()



