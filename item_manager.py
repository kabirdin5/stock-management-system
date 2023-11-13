class ItemManager:

    def __init__(self, items=None):
        self.items = []

    def get_items(self):
        return self.items

    def __str__(self):
        return "ItemManager({})".format(self.items)

    def __repr__(self):
        return str(ItemManager(self.items))

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    # Does not work
    def edit_item(self, old_item, new_item):
        self.items[self.items.index(old_item)] = new_item


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

    # Does not work
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

    def load_from_file(self, sample_data):
        pass

    def save_to_file(self, file_name):
        pass

    def list_items(self):
        return self.items
