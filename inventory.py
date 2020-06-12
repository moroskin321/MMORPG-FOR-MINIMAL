from item import Item
class Inventory:
    capacity = 10
    def __init__(self, items):
        self.items = items
a = Item('razor blade', 5, 50)
b = Item('abc', 3, 12)
c = [a, b]
i = Inventory(c)
