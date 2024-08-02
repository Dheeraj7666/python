
class Product:
    name = str()
    category = str()
    price = float()
    quantity = int()
    exp_date = int()
    products = list()

    def add_product_to_inventory(self):
        name = input("Enter the name of the product: ")
        category = input("Enter the category: ")
        price = float(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))
        exp_date = input("Enter the expiry date in format yr-mm-day: ")
        tup= tuple()
        tup = (name, category, price, quantity, exp_date)
        self.products.append(tup)
        print("Product added successfully")
        choice = 0
        choice_method(choice)

    def remove_product_from_inventory(self):
        name = input("Enter name: ")
        for product in self.products:
            if name in product:
                self.products.remove(product)
                print(f"Product with name {name} removed successfully.")
                break
        else:
            print(f"Product with name {name} not found.")
        choice_method(0)

    def list_all_products(self):
        print(self.products)
        choice_method(0)

    def search_products(self):
        search = input("Enter the name to search: ")
        search_list = [item for item in self.products if search in item]
        print(search_list)
        choice_method(0)

    def remove_expired_products(self):
        current_year = int(input("Enter the current year: "))
        current_month = int(input("Enter the current month: "))
        current_day = int(input("Enter the current day: "))
        current_date = (current_year, current_month, current_day)

        non_expired_products = []
        for product in self.products:
            year, month, day = map(int, product[4].split('-'))
            exp_date = (year, month, day)
            if exp_date >= current_date:
                non_expired_products.append(product)
        self.products = non_expired_products
        choice_method(0)

    def categorize_products(self):
        result_dict1 = {}
        for product in self.products:
            category = product[1]
            if category in result_dict1:
                result_dict1[category].append(product)
            else:
                result_dict1[category] = [product]
        print(result_dict1)
        choice_method(0)

    def save_inventory_to_file(self):
        with open("inventory.txt", 'w') as file:
            for product in self.products:
                file.write(str(product) + '\n')
        print("Product saved to file.")

    def load_inventory(self):
        try:
            with open("inventory.txt", "r") as file:
                for line in file:
                    data = line.strip()
                    self.products.append(data)
        except FileNotFoundError:
            print("No inventory file found.")


p = Product()

def enter_choice():
    print("1: Add product")
    print("2: Remove product")
    print("3: Search product")
    print("4: List product")
    print("5: Categorize product")
    print("6: Remove expired")
    print("7: Save and load inventory")
    print("8: Exit")
    choice = int(input("Enter choice: "))
    choice_method(choice)


def choice_method(choice):
    p.load_inventory()
    if choice == 0:
        enter_choice()
    elif choice == 1:
        p.add_product_to_inventory()
    elif choice == 2:
        p.remove_product_from_inventory()
    elif choice == 3:
        p.search_products()
    elif choice == 4:
        p.list_all_products()
    elif choice == 5:
        p.categorize_products()
    elif choice == 6:
        p.remove_expired_products()
    elif choice == 7:
        p.save_inventory_to_file()
    elif choice ==8:
        print("Exiting")
        exit()    
    else:
        print("Invalid choice")
        enter_choice()

enter_choice()