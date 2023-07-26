class Item:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def __repr__(self):
        return self.brand


items_list = [
    Item(1_000, 'Apple'),
    Item(1_200, 'Apple'),
    Item(900, 'Samsung'),
    Item(700, 'Samsung'),
    Item(660, 'Xiaomi'),
]
print(items_list[4])
print([item for item in items_list if item.brand == 'Samsung'])
print(list(filter(lambda item: item.brand == 'Samsung', items_list)))
print(items_list)

names_list = ['данил', 'артём', 'никита', 'влад']
print(list(map(lambda item: item[0].upper() + item[1:], names_list)))