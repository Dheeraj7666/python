
import json
from menu import MenuItem
from menu import ItemError

class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, menu, name, quantity):
        for item in menu.items:
            if item.name == name:
                if item.quantity >= quantity:
                    self.items.append(MenuItem(name, item.price, quantity))
                    item.quantity = item.quantity - quantity
                    return
                else:
                    raise lessQuantity(f"Not enough quantity for '{name}'. Available: {item.quantity}")
        raise ItemError(f"Item '{name}' not found in menu.")
    
    def calculate_total(self, discount=0):
        total = sum(item.price * item.quantity for item in self.items)
        return total * ((100 - discount) / 100)
    
    def receipt(self, discount=0):
        receipt = "Receipt:\n"
        for item in self.items:
            receipt += f"{item.name} - ${item.price:.2f} x {item.quantity} = ${item.price * item.quantity:.2f}\n"
        total = self.calculate_total(discount)
        receipt += f"Total after {discount}% discount: ${total:.2f}\n"
        print(receipt)
        return receipt

    def menu_file(self, filename='menu.txt'):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.items = [MenuItem(**item) for item in data]
        except FileNotFoundError:
            print(f"{filename} not found.")
    
    def order_file(self, filename='order.txt'):
        with open(filename, 'w') as file:
            json.dump([item.__dict__ for item in self.items], file)

class lessQuantity(Exception):
    pass
