"""
 Product klassi va Cart klassini yarating. 
Cart listda mahsulotlar saqlaydi
add_product(), remove_product(), total_price() metodlarini yozing.
Agar add_product() method i chaqirliganda mahsulot cartda bo’lsa maxsulot quantitysi oshib qolsin, remove_product()chaqirilganda mahsulot quantitysi kamayib qolsin agar quantity 0 bo’lib qolsa maxsulot cartdan olib tashlansin.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 


class Cart:
    def __init__(self):
        self.savat = []

    def add_product(self, new):
        self.savat.append(new)

    def remove_product(self, old):
        self.savat.remove(old)

    def look_it(self):
        for i in self.savat:
            print(i.name, i.price)

    def total_price(self):
        c = 0
        for i in self.savat:
            c+=i.price
        return c
    
i1 = Product("Olma", 12_000)
i2 = Product("Uzum", 10_000)
i3 = Product("Qulupnay", 35_000)
i4 = Product("Malina", 25_000)

c1 = Cart()

c1.add_product(i1)
c1.add_product(i2)
c1.add_product(i3)
c1.add_product(i4)

c1.remove_product(i2)

c1.look_it()

print(c1.checkout())