class Book:
    title = ''
    author = ''
    __year = 2000
    available = False
    number_of_copies_available = 0

    def __init__(self, title234, author, year, available):
        self.title = title234
        self.author = author
        self.__year = year
        self.available = available
        Book.number_of_copies_available += 1

    def display_details(self):
        print(f"Title: {self.title} \nWritten By: {self.author} \nYear: {self.__year}")
        if self.available:
            print(f"Available: Yes\n")
        else:
            print(f"Available: No\n")

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"The book has been borrowed")
            self.decrement_book()
        else:
            print(f"The book is already borrowed by someone else")


    def return_book(self):
        self.available = True
        print(f"The book has been returned")
        self.increment_book()
        # Book.number_of_copies_available += 1
        # print(f'The no. of books available: {Book.number_of_copies_available}')

    @classmethod
    def no_of_copies(cls):
        print(f'The no. of books available: {Book.number_of_copies_available}')

    @classmethod
    def increment_book(cls):
        Book.number_of_copies_available += 1

    @classmethod
    def decrement_book(cls):
        Book.number_of_copies_available -= 1

    @staticmethod
    def book_info():
        print("Books are man's best friend!!!")

book1 = Book("Atomic Habits", "Ankit Kumar", 2020, 1)
book2 = Book("Harri putter", "AAryan Pal", 2024, 1)
book1.display_details()
book2.display_details()
book1.borrow_book()
book1.borrow_book()
print("\n\nThe number of copies available are")
Book.no_of_copies()
book1.return_book()
book1.book_info()

book1.__year = 56780976
book1.display_details()


