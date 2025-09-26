"""Cart va Item klasslarini yarating. (20 ball)
1. Cart ichida mahsulotlar list ko‘rinishida saqlansin.
2. add_item(), remove_item(), checkout() metodlari bo‘lsin.
3. checkout() umumiy summani qaytarsin."""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price 


class Cart:
    def __init__(self):
        self.savat = []

    def add_item(self, new):
        self.savat.append(new)

    def remove_item(self, old):
        self.savat.remove(old)

    def look_it(self):
        for i in self.savat:
            print(i.name, i.price)

    def checkout(self):
        c = 0
        for i in self.savat:
            c+=i.price
        return c
    
i1 = Item("Olma", 12_000)
i2 = Item("Uzum", 10_000)
i3 = Item("Qulupnay", 35_000)
i4 = Item("Malina", 25_000)

c1 = Cart()

c1.add_item(i1)
c1.add_item(i2)
c1.add_item(i3)
c1.add_item(i4)

c1.remove_item(i2)

c1.look_it()

print(c1.checkout())

