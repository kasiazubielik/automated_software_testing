

class Student:
    def __init__(self, name, school, marks):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    
anna = Student("Anna", "MIT", [45])
anna.marks.append(56)
anna.marks.append(72)
print(anna.marks)
print(anna.average())


##

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        total = 0
        for item in self.items:
            total += sum(item[price])
        return total
        return sum([item[price] for item in self.items])
    # Add together all item prices in self.items and return the total.
