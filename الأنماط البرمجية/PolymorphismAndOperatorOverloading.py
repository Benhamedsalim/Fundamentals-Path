class Point:
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__ (self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__ (self):
        return f'x: {self.x}, y: {self.y}, z: {self.z}'
pt1 = Point(3, 4, -5)
pt2 = Point(-4, 1, 3)
pt3 = pt1 + pt2
print(pt3)

class Cart:
    def __init__ (self, items):
        self.items = items
    def __getitem__ (self, key):
        return self.items[key]

order1 = Cart(['Pen', 'Pencil', 'Notebook' ])

print(order1.items[0])
print(order1[0])