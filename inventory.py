from item import Item
class Inventory:
    capacity = 0
    capacity_max = 2
    def __init__(self, items):
        if len(items) <= self.capacity_max:
            self.items = items
            self.capacity += len(items)
        else:
            self.items = items[:self.capacity_max]
            self.capacity = self.capacity_max

    def add_item(self, new_item):
        if self.capacity < self.capacity_max:
            self.items.append(new_item)
            self.capacity += 1

    def delete_item(self, i):
        if i < capacity and i >= 0:
            self.items = self.items[:i] + self.items[i+1:]
            self.capacity -= 1

a = Item('razor blade', 5, 50)
b = Item('abc', 3, 12)
d = Item('DEAD SEA SCROLLS', 5, 16)
c = [a]
i = Inventory(c)
print(i.capacity, end = ' from ')
print(i.capacity_max)
for j in range(0, i.capacity):
    print(i.items[j].name)
