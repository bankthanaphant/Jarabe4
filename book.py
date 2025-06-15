class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def summary(self):
        return print(self.title + " " + self.author + " " + str(self.pages) + " Pages")

book1 = Book("calculus1", "ens", 159)
book2 = Book("Compro1", "chiabwoot", 201)

book1.summary()
book2.summary()