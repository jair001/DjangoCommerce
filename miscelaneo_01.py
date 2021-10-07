# dado lista de items
items = [
    {'name': "item a", 'pvp': 10, 'bodega': "A"},
    {'name': "item b", 'pvp': 20, 'bodega': "A"},
    {'name': "item c", 'pvp': 30, 'bodega': "B"},
    {'name': "item d", 'pvp': 40, 'bodega': "C"},
    {'name': "item e", 'pvp': 5, 'bodega': "B"},
]


# 1 desplegar los items de bodega A y C
def items_by_warehouse(products: list, name_warehouse: str = ''):
    message = ""
    for product in products:
        if product.get("bodega") == "A" or product.get("bodega") == "C":
            # ejm None, en lugar de None devuelve un texto defindo x el usuario ene ste caso "no existe"
            c = product.get("xyz","no existe")
            print(c)
            message = message + "\n" + product.get("name")
    return message


response = items_by_warehouse(products=items)
print(response)


# si no encuentra datos en una consulta devuelve None

# list comprehension
result = [item.get('name') for item in items if item.get("bodega") == "A" or item.get("bodega") == "C"]
print(result)

# 2. Deplegar el total pvp de items de la bodega B
def total_by_warehouse(products: list):
    message = ""
    total = 0
    for product in products:
        if product.get("bodega") == "B":
            message = message + "\n" + product.get("name")
            total = total + product.get("pvp")
    message = message + f"\n total pvp {total}"
    return message

result = total_by_warehouse(products=items)
print(result)