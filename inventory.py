#inventory
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                raise Exception("Invalid quantity.")
        else:
            raise Exception("Item not found.")

    def check_item(self, item_name):
        return self.items.get(item_name, 0)

    def print_inventory(self):
        if not self.items:
            print("The inventory is empty.")
        else:
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")
                
    def list_items(self):
        if not self.items:
            print("The inventory is empty.")
        else:
            print("Inventory Items:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")           

# Create an instance of Inventory
inventory = Inventory()
inventory.add_item("apples",10)
inventory.add_item("oranges",7)
inventory.add_item("bananas",5)


inventory.remove_item("apples",2)

inventory.list_items()


