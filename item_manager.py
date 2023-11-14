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
            if item.get_category() == category:
                category_items.append(item)
        return category_items

    def search_by_perishable(self, perishable):
        perishable_items = []
        for item in self.items:
            if item.get_perishable() == perishable:
                perishable_items.append(item)
        return perishable_items

    def search_by_sell_price(self, sell_price):
        priced_items = []
        for item in self.items:
            if item.get_sell_price() == sell_price:
                priced_items.append(item)
        return priced_items

    def apply_discount_to_items(self, names, discount):
        discounted_items = []
        for name in names:
            for item in self.items:
                if item.name == name:
                    item.sell_price = item.get_sell_price() * (1 - (discount / 100))
                    discounted_items.append(item)
        return discounted_items

    def purchase_available_items(self, names, is_member):
        total_cost = 0
        for name in names:
            for item in self.items:
                if item.get_name() == name:
                    if item.get_stock() > 0:
                        item.stock = item.get_stock() - 1
                        total_cost = total_cost + item.get_sell_price()
                    elif item.get_stock() == 0:
                        print(name + " is out of stock")
        if is_member:
            if total_cost >= 50:
                total_cost = total_cost * 0.9
            else:
                total_cost = total_cost * 0.95
        return total_cost

    def load_from_file(self, file_name):
        current_stock = []
        with open(file_name) as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                [name, category, perishable, stock, sell_price] = row[0], row[1], bool(row[2]), int(row[3]), float(row[4])
                item = Item(name, category, perishable, stock, sell_price)
                current_stock.append(item)
            return current_stock

    def save_to_file(self, file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "category", "perishable", "stock", "sell_price"])
            for item in self.items:
            #for item in range(0, len(self.items)):
                writer.writerow([self.items[item].get_name(), self.items[item].get_category(),
                                 self.items[item].get_perishable(), self.items[item].get_stock(),
                                 self.items[item].get_sell_price()])

    def list_items(self):
        return self.items
