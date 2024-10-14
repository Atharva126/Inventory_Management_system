class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def update_price(self, new_price):
        self.price = new_price

    def total_value(self):
        return self.quantity * self.price


class InventoryManagementSystem:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.items = []

    def login(self):
        print("Please log in to access the Inventory Management System.")
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")

        if entered_username == self.username and entered_password == self.password:
            print("Login successful!")
            self.run()
        else:
            print("Invalid username or password. Access denied.")

    def add_item(self, name, quantity, price):
        self.items.append(Item(name, quantity, price))
        print(f"Item '{name}' added successfully.")

    def remove_item(self, name):
        for i, item in enumerate(self.items):
            if item.name == name:
                del self.items[i]
                print(f"Item '{name}' removed successfully.")
                return
        print(f"Item '{name}' not found.")

    def update_item_quantity(self, name, new_quantity):
        for item in self.items:
            if item.name == name:
                item.update_quantity(new_quantity)
                print(f"Item '{name}' quantity updated to {new_quantity}.")
                return
        print(f"Item '{name}' not found.")

    def update_item_price(self, name, new_price):
        for item in self.items:
            if item.name == name:
                item.update_price(new_price)
                print(f"Item '{name}' price updated to {new_price}.")
                return
        print(f"Item '{name}' not found.")

    def search_item(self, name):
        for item in self.items:
            if item.name == name:
                self.display_single_item(item)
                return
        print(f"Item '{name}' not found.")

    def display_single_item(self, item):
        print("\nItem found:")
        print(f"+{'-'*10}+{'-'*10}+{'-'*10}+")
        print(f"| {'Name':<8} | {'Quantity':<8} | {'Price':<8} |")
        print(f"+{'-'*10}+{'-'*10}+{'-'*10}+")
        print(f"| {item.name:<8} | {item.quantity:<8} | {item.price:<8} |")
        print(f"+{'-'*10}+{'-'*10}+{'-'*10}+\n")

    def display_inventory(self):
        if not self.items:
            print("No items in inventory.")
            return
        print("\nInventory:")
        print(f"+{'-'*15}+{'-'*10}+{'-'*10}+{'-'*15}+")
        print(f"| {'Item Name':<13} | {'Quantity':<8} | {'Price':<8} | {'Total Value':<13} |")
        print(f"+{'-'*15}+{'-'*10}+{'-'*10}+{'-'*15}+")
        for item in self.items:
            print(f"| {item.name:<13} | {item.quantity:<8} | {item.price:<8} | {item.total_value():<13} |")
        print(f"+{'-'*15}+{'-'*10}+{'-'*10}+{'-'*15}+\n")

    def display_total_inventory_value(self):
        total_value = sum(item.total_value() for item in self.items)
        print(f"Total inventory value: {total_value}")

    def sort_inventory(self, key='name', reverse=False):
        self.items.sort(key=lambda item: getattr(item, key), reverse=reverse)
        print(f"Inventory sorted by {key} {'descending' if reverse else 'ascending'} order.")

    def filter_items_by_price(self, min_price, max_price):
        filtered_items = [item for item in self.items if min_price <= item.price <= max_price]
        if filtered_items:
            for item in filtered_items:
                self.display_single_item(item)
        else:
            print(f"No items found in the price range {min_price} to {max_price}.")

    def run(self):
        while True:
            print("\nInventory Management System Menu:")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Update Item Quantity")
            print("4. Update Item Price")
            print("5. Search Item")
            print("6. Display Inventory")
            print("7. Display Total Inventory Value")
            print("8. Sort Inventory")
            print("9. Filter Items By Price")
            print("10. Exit")

            choice = input("Enter your choice (1-8): ")

            if choice == '1':
                name = input("Enter item name: ")
                quantity = int(input("Enter item quantity: "))
                price = float(input("Enter item price: "))
                self.add_item(name, quantity, price)

            elif choice == '2':
                name = input("Enter item name to remove: ")
                self.remove_item(name)

            elif choice == '3':
                name = input("Enter item name to update quantity: ")
                new_quantity = int(input("Enter new quantity: "))
                self.update_item_quantity(name, new_quantity)

            elif choice == '4':
                name = input("Enter item name to update price: ")
                new_price = float(input("Enter new price: "))
                self.update_item_price(name, new_price)

            elif choice == '5':
                name = input("Enter item name to search: ")
                self.search_item(name)

            elif choice == '6':
                self.display_inventory()

            elif choice == '7':
                self.display_total_inventory_value()
            
            elif choice == '8':
                self.sort_inventory()

            elif choice == '9':
                min_price=input("Enter minimum Price:")
                max_price=input("Enter maximum Price:")
                self.filter_items_by_price(min_price,max_price)

            elif choice == '10':
                print("Exiting Inventory Management System. Goodbye!")
                break

            else:
                print("Invalid choice! Please select a valid option.")

# Start the interactive inventory management system
if __name__ == "__main__":
    ims = InventoryManagementSystem(username="admin",password="pass@123")
    ims.login()
