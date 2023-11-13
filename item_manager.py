import csv
from item import Item

class ItemManager:

    def __init__(self, items=None):
        self.items = []

    def get_items(self):
        return self.items

    def __str__(self):
        return "ItemManager({})".format(self.items)

    def __repr__(self):
        return ItemManager(self.items)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    # Does not work
    def edit_item(self, old_item, new_item):
        if old_item in self.items:
            old_item_pos = self.items.index(old_item)
            self.items.remove(old_item)
            self.items.insert(old_item_pos, new_item)

    def search_by_category(self, category):
        category_items = []
        for item in self.items:
            if item.category == category:
                category_items.append(item)
        return category_items

    def search_by_perishable(self, perishable):
        perishable_items = []
        for item in self.items:
            if item.perishable == perishable:
                perishable_items.append(item)
        return perishable_items

    def search_by_sell_price(self, sell_price):
        priced_items = []
        for item in self.items:
            if item.sell_price == sell_price:
                priced_items.append(item)
        return priced_items

    def apply_discount_to_items(self, names, discount):
        discounted_items = []
        for name in names:
            for item in self.items:
                if item.name == name:
                    item.sell_price = item.sell_price * (1 - (discount / 100))
                    discounted_items.append(item)
        return discounted_items

    def purchase_available_items(self, names, is_member):
        total_cost = 0
        for name in names:
            for item in self.items:
                if item.name == name:
                    if item.stock > 0:
                        item.stock = item.stock - 1
                        total_cost = total_cost + item.sell_price
                    elif item.stock == 0:
                        print(name + " is out of stock")
        if is_member:
            if total_cost >= 50:
                total_cost = total_cost * 0.9
            else:
                total_cost = total_cost * 0.95
        return total_cost

    def load_from_file(self, file_name):
        #try:
        """
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)
            #for row in reader:
             #   name, category, perishable, stock, sell_price = row
              #  item = Item(name, category, perishable, stock, sell_price)
               # self.items.append(item)

            for row in reader:
                item = Item(row['name'], row['category'], row['perishable'], row['stock'], row['price'])
                self.items.append(item)

                #print("Items loaded successfully")
        """
        current_stock = []
        with open(file_name) as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                #item.get_name, item.category, item.perishable, item.stock, item.sell_price = row
                #item = Item(item.get_name, item.category, item.perishable, item.stock, item.sell_price)
                current_stock.append(row)
            return current_stock

    def save_to_file(self, file_name):
        pass


    def list_items(self):
        return self.items
