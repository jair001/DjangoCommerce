# crear clase de ordenes
# order(created_at, code, warehouse, items, total_quantity, total_amount)

import datetime
from decimal import Decimal
from random import randrange
import uuid

products = [
    {'name': "item a", 'pvp': 10, 'bodega': "A"},
    {'name': "item b", 'pvp': 20, 'bodega': "A"},
    {'name': "item c", 'pvp': 30, 'bodega': "B"},
    {'name': "item d", 'pvp': 40, 'bodega': "C"},
    {'name': "item e", 'pvp': 5, 'bodega': "B"},
]


def generate_unique_code():
    frame = datetime.datetime.now().strftime("%S%f")  # dada fecha actual (objeto datetime)
    print(frame)
    print(uuid.uuid4())
    code = str(uuid.uuid4()).split("-")
    unique_code = f"{code[0]}{frame}"
    return unique_code

print(generate_unique_code())

class OrderModel:

    # constructor
    def __init__(self, created_at: datetime,  # code: str,
                 warehouse: dict, items: []):

        self.created_at = created_at
        # self.code = randrange(1000, 9999, 2)  # code
        self.code = generate_unique_code()
        self.warehouse = warehouse
        self.items = items
        self.total_qty = 0
        self.total_amount = 0

    # metodo cantidad de items
    # metodo total monto de items

    # METODOS DE INSTANCIA
    def set_total_quantity(self):
        self.total_qty = len(self.items)

    def set_total_amount(self):
        total = 0
        for item in self.items:
            total += item.get('pvp')
        self.total_amount = total

    # def get_codigo(self):
    #    self.code = randrange(1000, 9999, 2)

    # METODOS ESTATICOS


warehouse_a = {"code": "A", "name": "Bodega A" }
order_a = OrderModel(created_at=datetime.datetime.now(), warehouse=warehouse_a, items=products) # code='0001'
order_a.set_total_quantity()
order_a.set_total_amount()
order_b = OrderModel(created_at=datetime.datetime.now(), warehouse=warehouse_a, items=[])
print(f"Orden: {order_b.code}")
print(f"cantidad de items {order_a.total_qty}")
print(f"valor total del pedido: {order_a.code} es:  {order_a.total_amount}")
