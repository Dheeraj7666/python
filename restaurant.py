from order import lessQuantity
from menu import ItemError
from menu import Menu
from order import Order

def shop():
    menu = Menu()
    menu.menu_file()
    
    order = Order()
    while True:
        print("\n1. Add Menu")
        print("2. Update Menu")
        print("3. Delete Menu")
        print("4. Display Menu")
        print("5. Place Order")
        print("6. View Order")
        print("7. Generate Receipt")
        print("8. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                name = input("product name: ")
                price = float(input("price: "))
                quantity = int(input("quantity: "))
                menu.add_item(name, price, quantity)
            except ItemError as e:
                print(e)

        elif choice == '2':
            try:
                name = input("product name: ")
                price = float(input("price: "))
                quantity = int(input("quantity: "))
                menu.update_item(name, price, quantity)
            except ItemError as e:
                print(e)

        elif choice == '3':
            try:
                name = input("product name: ")
                menu.delete_item(name)
            except ItemError as e:
                print(e)
        elif choice == '4':
            menu.display_menu()

        elif choice == '5':
            try:
                name = input("product name: ")
                quantity = int(input("Quantity: "))
                order.add_item(menu, name, quantity)
            except (ItemError, lessQuantity) as e:
                print(e)

        elif choice == '6':
            print("Current Order:")
            for item in order.items:
                print(item)
        
        elif choice == '7':
            try:
                discount = float(input("Discount percentage:"))
                order.receipt(discount)
            except ValueError:
                print("Invalid input.")
        
        elif choice == '8':
            menu.menu_file()
            order.order_file()
            print("Exiting...")
            break
        
        else:
            print("Invalid choice")
shop()