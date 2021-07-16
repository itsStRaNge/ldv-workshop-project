from lib.database import DatabaseConnector


class BooksDB:
    def __init__(self):
        self.receipts = DatabaseConnector("receipts")

    def add_book(self, book):
        pass

    def update_book(self, receipt):
        pass

    def find_book(self, book_id):
        return {}
