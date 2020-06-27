# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author_first_name, author_last_name):
        self.title = title
        self.price = price

        self.author_first_name = author_first_name
        self.author_last_name = author_last_name

        self.chapters = []

    def add_chapter(self, name, pages):
        self.chapters.append((name, pages))


b1 = Book("War and Peace", 39.0, "Leo", "Tolstoy")

b1.add_chapter("Chapter 1", 125)
b1.add_chapter("Chapter 2", 97)
b1.add_chapter("Chapter 3", 143)

print(b1.title)
