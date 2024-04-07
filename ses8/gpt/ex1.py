"""
Exercise 1: Create a Simple Class
Create a Python class named Book that has two attributes: title and author. Then, create a method within this class named get_description that returns a string like "Title by Author", replacing Title and Author with the respective attribute values. Finally, instantiate an object of this class with the title "To Kill a Mockingbird" and the author "Harper Lee", and use the get_description method to print the description of the book.
"""

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_description(self):
        return f'{self.title} by {self.author}'

book = Book('To Kill a Mockingbird', 'Harper Lee')
print(book.get_description())
