from lib.database import DatabaseConnector


class ReceiptsDB:
    def __init__(self):
        self.receipts = DatabaseConnector("receipts")

    def add_receipt(self, receipt):
        pass

    def remove_receipt(self, receipt_id):
        pass

    def update_receipt(self, receipt):
        pass

    def get_receipt(self, receipt_id):
        return ""
