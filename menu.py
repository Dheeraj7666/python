# menu.py

import json

class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} - ${self.price:.2f} (Quantity: {self.quantity})"

class Menu:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity):
        if any(item.name == name for item in self.items):
            raise ItemError(f"Item '{name}' already exists.")
        self.items.append(MenuItem(name, price, quantity))
    
    def update_item(self, name, price, quantity):
        for item in self.items:
            if item.name == name:
                item.price = price
                item.quantity = quantity
                return
        raise ItemError(f"Item '{name}' not found.")
    
    def delete_item(self, name):
        self.items = [item for item in self.items if item.name != name]
    
    def display_menu(self):
        for item in self.items:
            print(item)
    
    def menu_file(self, filename='menu.txt'):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.items = [MenuItem(**item) for item in data]
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty menu.")
    
    def menu_file(self, filename='menu.txt'):
        with open(filename, 'w') as file:
            json.dump([item.__dict__ for item in self.items], file)

class ItemError(Exception):
    pass
