from core.db_manager import DBModel
from datetime import datetime


class Cashier(DBModel):
    def __init__(self, _id, name, last_name, email, phone, password) -> None:
        self._id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password


class CafeTable(DBModel):
    def __init__(self, _id, number, space) -> None:
        self._id = _id
        self.number = number
        self.space = space


class MenuItems(DBModel):

    def __init__(self, _id, category_id, discount, name, price, img_url, serving_time) -> None:
        self._id = id
        self.category_id = category_id
        self.name = name
        self.discount = discount
        self.price = price
        self.img_url = img_url
        self.serving_time = serving_time


class Table(DBModel):
    def __init__(self, _id, number, space):
        self.id = _id
        self.number = number
        self.space = space


class Status(DBModel):
    def __init__(self, _id, name, description):
        self.id = _id
        self.name = name
        self.description = description


class Category(DBModel):
    _id: int
    name: str
    category_id: int

    def __init__(self, _id, name, category_id=None):
        self._id = _id
        self.name = name
        self.category_id = category_id


class Order(DBModel):
    def __init__(self, _id, item_id, number_items, receipt_id, status_id, table_id):
        self._id = id
        self.item_id = item_id
        self.number_items = number_items
        self.receipt_id = receipt_id
        self.status_id = status_id
        self.table_id = table_id
        self.time_stamp = datetime.now()


class Receipt(DBModel):
    def __init__(self, _id, total_price, final_price) -> None:
        self._id = _id
        self.total_price = total_price
        self.final_price = final_price
        self.time_stamp = datetime.now()

