class Book:
    title=""
    author=""
    year=2000
    available= True

    def __init__(self,t1,a1,y1,available1):
        self.title=t1
        self.author=a1
        self.year=y1
        self.available=available1

    def display_details(self):
        print(f"Title:{self.title},self.author,self.year,self.available")
        if self.available==True:
            print(f"Available")
        else:
            print(f"Not Available")

    def borrow_book(self):
        if self.available=False:
            print("Already borrowed")

