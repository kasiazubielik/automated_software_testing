
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_numbers():
    evens = []
    for number in numbers:
        evens.append(number)
    return evens

print(even_numbers(evens))

##

# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = { "name": "Jose", "school": "Computing", "grades": (66, 77, 88) }

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =  data['grades']  # we have to access a key in a dictionary! tha variable grades now has access to 'grades'key in dictionary
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (dictionaries), calculate the average grade of the class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total = total + sum(student['grades']) # (total = total + sum..) can be shown as (total += sum...)
        count = count + len(student['grades'])

    return total / count

##

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        item = {"name": name, "price": price}
        fruit.item = {"apple": (60), "banana": (80), "lemon": (45)}
        self.items.append(item)
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        total = 0
        for item in self.items:
            total += sum(item["price"])
        return total
        return sum([item[price] for item in self.items])


##

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        new_store = Store(store.name + " - franchise")
        return new_store
        # return cls(store.name + " - franchise")
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        print("{}, total stock price: + {}").format(store.name, int(store.stock))
    # It should be in the format 'NAME, total stock price: TOTAL'

    
