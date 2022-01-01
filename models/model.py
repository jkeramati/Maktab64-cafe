from core.db_manager import DBModel
from datetime import datetime

class Cashier(DBModel):
    def __init__(self, id, name, last_name, email, phone, password) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password




class Order(DBModel):
    def __init__(self,id, item_id, number_items, receipt_id, status_id, table_id):
        self.id = id
        self.item_id = item_id
        self.number_items = number_items
        self.receipt_id = receipt_id
        self.status_id = status_id
        self.table_id = table_id
        self.time_stamp = datetime.now()