class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, int):
            return self.price - other
        elif isinstance(other, Item):
            return self.price - other.price

    def __sub__(self, other):
        if isinstance(other, int):
            return self.price - other
        elif isinstance(other, Item):
            return self.price - other.price

    def __mul__(self, other):
        if isinstance(other, int):
            return self.price * other
        elif  isinstance(other, Item):
            print('Ты чё творишь!!!')

    def __truediv__(self, other):
        if isinstance(other, int):
            return int(self.price / other)
        elif  isinstance(other, Item):
            return int(self.price / other.price)


a = [Item('Монитор', 20_000, 5),
     Item('Видеокарта', 15_000, 0.8)
     ]


print(a[0] + a[1])
print(a[0] - a[1])
print(a[0] * 5)
print(a[0] / 2)
print(sum([x.price for x in a]))