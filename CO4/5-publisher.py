class Publisher:
    def __init__(self, name):
        self.name = name

class Book(Publisher):
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Python(Book):
    def __init__(self, price, pages):
        self.price = price
        self.pages = pages
        
book1 = Python(200, 37);

print("\nPython:\nPrice: "+str(book1.price)+"\nPages: "+str(book1.pages)+"\n")
