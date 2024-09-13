class Book:
    title=""
    author=""
    year=2000
    available=True
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year

    def display_info(self):
        print(self.title,self.author,self.year)

        if self.available:
            print("You can borrow the book")
        else:
            print("The book is not available")


ob1=Book("Atomic Theory","Aryan", 1992)
print(ob1.title)
print(ob1.display_info())


