from lib.database import DatabaseConnector


class LogDB:

    def __init__(self):
        self.log = DatabaseConnector("logs.db")

    def add_log(self):
        pass