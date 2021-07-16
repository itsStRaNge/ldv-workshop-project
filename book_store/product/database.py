from lib.database import DatabaseConnector


class Database:

    def __init__(self):
        self.receipts = DatabaseConnector("receipts.db")
        self.logs = DatabaseConnector("logs.db")
