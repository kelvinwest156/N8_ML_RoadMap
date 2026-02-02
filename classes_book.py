class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Magic methods
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages


book1 = Book(title="The Great Controversy", author="Ellen G. White", pages=504)

print(book1)
print(len(book1))