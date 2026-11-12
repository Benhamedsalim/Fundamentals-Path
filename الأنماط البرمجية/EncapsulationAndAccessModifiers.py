class Product:
    def __init__ (self, id, name, price, count):
        self.id = id
        self.name = name
        self.price = price
        self.count = count

    def discount(self, ratio):
        self.price = self.price - self.price*ratio

    def info(self):
        return f'id: {self.id}, Name: {self.name}, Price: {self.price}$, Count: {self.count}'

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return str(self.price) + '$'

iphone_13 = Product(id=1, name='iphone 13', price=999, count=12)

iphone_13.price = 0
print(iphone_13.info())

class Product:
    def __init__ (self, id, name, price, count):
        self.id = id
        self.name = name
        self .__price = price
        self.count = count

    def discount(self, ratio):
        self .__price = self.__price - self.__price*ratio

    def info(self):
        return f'id: {self.id}, Name: {self.name}, Price: {self.__price}$, Count: {self.count}'

    def set_price(self, price):
        self .__price = price

    def get_price(self):
        return str(self.__price) + '$'

iphone_13 = Product(id=1, name='iphone 13', price=999, count=12)

iphone_13.__price = 0

print(iphone_13.info())

print(iphone_13.__price)

iphone_13.Productr_price = 0

print(iphone_13.info())