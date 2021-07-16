from book_store.cloud import Cloud
from book_store.database import Database
from book_store.hardware import Hardware


class MyProject:
    def __init__(self):
        self.cloud = Cloud()
        self.database = Database()
        self.hardware = Hardware()

    def run(self):
        pass


MyProject().run()
