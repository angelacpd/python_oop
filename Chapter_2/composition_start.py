# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def get_book_page_count(self):
        result = 0
        for ch in self.chapters:
            result += ch.page_count
        return result


class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Chapter:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count


author1 = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, author1)

b1.add_chapter(Chapter("Chapter 1", 125))
b1.add_chapter(Chapter("Chapter 2", 97))
b1.add_chapter(Chapter("Chapter 3", 143))

print(b1.author)
print(b1.title)
print(b1.get_book_page_count())
