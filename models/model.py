from core.db_manager import DBModel, DBManager
from datetime import datetime, timedelta


class Cashier(DBModel):
    TABLE = "cashier"
    aliases = {"_id": "id"}

    def __init__(self, name, last_name, email, phone, password, _id=None) -> None:
        self.alias_for("_id", "id")
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password
        if _id:
            self._id = _id


class CafeTable(DBModel):
    TABLE = "cafe_table"

    def __init__(self, number, space, id) -> None:
        self.number = number
        self.space = space
        self.id = id


class MenuItems(DBModel):
    TABLE = 'menu_items'

    def __init__(self, category_id, discount, name, price, image_url, serving_time, id=None) -> None:
        self.category_id = category_id
        self.name = name
        self.discount = discount
        self.price = price
        self.image_url = image_url
        self.serving_time = serving_time
        if id: self.id = id


class Status(DBModel):
    TABLE = "status"

    def __init__(self, name, description, id=None):
        self.name = name
        self.description = description
        if id: self.id = id


class Category(DBModel):
    TABLE = "categories"

    def __init__(self, name, category_id=None, id=0):
        self.name = name
        self.category_id = category_id
        self.id = id


class Order(DBModel):
    TABLE = "orders"

    def __init__(self, item_id, number_item, receipt_id, status_id, table_id, id=0):
        self.item_id = item_id
        self.number_item = number_item
        self.receipt_id = receipt_id
        self.status_id = status_id
        self.table_id = table_id
        self.time_stamp = datetime.now()
        self.id = id


class Receipt(DBModel):
    TABLE = "receipt"

    def __init__(self, total_price, final_price, id=0) -> None:
        self.total_price = total_price
        self.final_price = final_price
        self.time_stamp = datetime.now()
        self.id = id


# cat = Category("cake")
# db1 = DBManager().create(cat)
# time_t = datetime.now() + timedelta(minutes=10)
# item = MenuItems(1, 0, 'cake', 50000, 'img_url', time_t)
# db = DBManager().create(item)
# cashier = Cashier("cashier", "cashier_id", "example@gmail.com", "0987654321111", "0234832")
# DBManager().create(cashier)
# tbl = CafeTable(1, 3, 1)
# dbt = DBManager().create(tbl)
# stat = Status('error', 'Error from server!', 1)
# dbs = DBManager().create(stat)
# rece = Receipt(5000, 4999, 1)
# dbr = DBManager().create(rece)
# order = Order(0, 10, 1, 1, 1)
# dbr = DBManager().create(order)
# dbdel = DBManager().delete(order)  # for_test
# print(DBManager().query("SELECT * FROM cashier", fetch="all"))
# print(len(DBManager().query("SELECT * FROM cashier", fetch=2)))