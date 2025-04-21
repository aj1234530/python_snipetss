# problem statement
# library manangement:

# book class
# library class

# add book 
# remove book
# search book

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
class Library:

#use the instance variable not class variable as 
# each library should have its own collection
    total_books = 0
    books = []

    def add_book(self,book):
        Library.total_books += 1
        Library.books.append(book)
    def remove_book(self,title,author):
        for book in Library.books:
            if (book.title == title and book.author == author ):
                self.books.remove(book)
    def search_book(self,title,author):
        results = []
        for book in Library.books:
            if(book.title == title or book.author == author):
                results.append(book)
        return results
b1 = Book("book1","author1")
b2 = Book("book2","author2")
