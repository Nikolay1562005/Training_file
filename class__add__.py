class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    def __add__(self, other):
        if isinstance(other, int):
            return self.price + other
        elif isinstance(other, int):
            return self.price + other.price

a = [Item('Монитор', 20_000, 5),
     Item('Видеокарта', 15_000, 0.8)
]
print(a[0].price + a[1].price)
print(sum([x.price for x in a]))
print(type(500), isinstance(500, Item), sep='\n')