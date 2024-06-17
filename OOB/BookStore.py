import Book, Author, Publisher

class BookStore(Book, Author, Publisher):
    def __init__(self, name) -> None:
        self.name = name
        self.inventory = {}
        self.sales = 0
        
    def add_book(self, book, quantity):
        if book.book_id not in self.inventory:
            self.inventory[book.book_id] = {'book':book, 'quantiy':quantity}
            print(f'Added {quantity} copies of {book.title} to the inventory')
    
    def sell_books(self, book_id, quantity, discount_percent = 0):
        pass