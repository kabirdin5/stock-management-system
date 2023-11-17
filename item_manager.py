import csv  # Imports a module used for reading and writing the CSV files
from item import Item  # Imports the Item class from the item.py file

class ItemManager:
    # Creates the ItemManager class
    def __init__(self, items=None):
        """
        Initialises an ItemManager object
        :param items (list): list of Item objects
        """
        if items is None:
            # Initialises an empty list if the "items" parameter is not provided
            self.items = []

    def get_items(self):
        # Gets the list of items as an object and returns it
        return self.items

    def __str__(self):
        # Creates a string representation of the ItemManager and returns it
        return "ItemManager({})".format(self.items)

    def __repr__(self):
        # Creates a more official representation of the ItemManager and returns it
        return ItemManager(self.items)

    def add_item(self, item):
        # Adds an item to the ItemManager
        self.items.append(item)

    def remove_item(self, item):
        # Removes an item from the ItemManager
        self.items.remove(item)

    def edit_item(self, old_item, new_item):
        """
        Edits an existing item from ItemManager
        :param old_item: item that is already existing in ItemManager
        :param new_item: item that is to replace old_item
        """
        if old_item in self.items:  # If old_item is found in itemsManager
            old_item_pos = self.items.index(old_item)  # Creates a variable containing the index position of old_item
            self.items.remove(old_item)  # Removes old_item from ItemsManager
            self.items.insert(old_item_pos, new_item)  # Inserts the new_item into the same position as old_item

    def search_by_category(self, category):
        """
        Searches for the items by category
        :param category: The category to search for
        :return category_items: returns a list containing the items of the specific category
        """
        category_items = []  # Creates an empty list containing the categorised items
        for item in self.items:
            # For every item in ItemManager that is in the specific category,
            # they are added to the "category_items" list
            if item.get_category() == category:
                category_items.append(item)
        return category_items

    def search_by_perishable(self, perishable):
        """
        Searches for the items by their perishable status
        :param perishable: The perishable status to search for
        :return perishable_items: returns a list containing the items with the specific perishable status given
        """
        perishable_items = []  # Creates an empty list containing the items with the specific perishable status
        for item in self.items:
            # For every item in ItemsManager that has the specific perishable status,
            # they are added to the "perishable_items" list
            if item.get_perishable() == perishable:
                perishable_items.append(item)
        return perishable_items

    def search_by_sell_price(self, sell_price):
        """
        Searches for the items by their sell_price
        :param sell_price: The selling price to search for
        :return priced_items: returns a list containing the items with the specific selling price to search for
        """
        priced_items = []  # Creates an empty list containing the items with the searched price
        for item in self.items:
            # For every item in ItemsManager that has the searched price,
            # they are added to the "priced_items" list
            if item.get_sell_price() == sell_price:
                priced_items.append(item)
        return priced_items

    def apply_discount_to_items(self, names, discount):
        """
        Applies the discount to the chosen items from ItemsManager
        :param names: The list of item names
        :param discount: The discount applied to the selling prices of the items
        :return discounted_items: returns a list containing the items where their prices were discounted
        """
        discounted_items = []  # Creates an empty list containing the items to be discounted
        if 0 <= discount <= 50:  # The discount can only be between 0% and 50%
            for name in names:
                for item in self.items:
                    # For every item in ItemsManager that is chosen to get discounted,
                    # the selling price is altered according to the discount given.
                    # The discounted items are then added to the list
                    if item.name == name:
                        item.sell_price = item.get_sell_price() * (1 - (discount / 100))
                        discounted_items.append(item)
            return discounted_items

    def purchase_available_items(self, names, is_member):
        """
        Calculates the total cost for the chosen purchased items and updates the stock.
        Also, being a member has an effect on the total cost
        :param names: The name of the item chosen to purchase
        :param is_member: Determines whether the user is a member or not
        :return total_cost: returns the total cost of all the items purchased
        """
        total_cost = 0  # The total cost starts at 0
        for name in names:
            for item in self.items:
                # For every item in ItemsManager, if the stock of that item is more than 0, it decrements by 1.
                # Also, each item's selling price is added to the total cost.
                if item.get_name() == name:
                    if item.get_stock() > 0:
                        item.stock = item.get_stock() - 1
                        total_cost = total_cost + item.get_sell_price()
                    elif item.get_stock() == 0:
                        print(name + " is out of stock")
        if is_member:
            # If the user is a member
            if total_cost >= 50:
                # If the total cost is equal or more than 50,
                # The total cost is discounted by 10%
                total_cost = total_cost * 0.9
            else:
                # Else, the total cost is discounted by 5%
                total_cost = total_cost * 0.95
        return total_cost

    def load_from_file(self, file_name):
        """
        Loads the items from the csv file
        :param file_name: The name of the csv file
        :return current_stock: returns the list of items that contains the items loaded from the csv file
        """
        current_stock = []  # Creates an empty list containing the items loaded from the csv file
        with open(file_name) as file:
            reader = csv.reader(file)
            next(reader)  # Skips the header row
            for row in reader:
                # The values from every row is extracted from the csv file and given their attribute
                [name, category, perishable, stock, sell_price] = row[0], row[1], bool(row[2]), int(row[3]), float(
                    row[4])
                # Item objects are created using the values extracted from the csv file
                item = Item(name, category, perishable, stock, sell_price)
                current_stock.append(item)  # Each item is added to the "current_stock" list
            return current_stock

    def save_to_file(self, file_name):
        """
        Writes the given items to a csv file which is separate from the sample_data
        :param file_name: The name of the csv file
        """
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            # Creates the header row of the csv file, which is the same as the sample_data
            writer.writerow(["name", "category", "perishable", "stock", "sell_price"])
            for item in self.items:
                # For every item in ItemManager, the details of each item are written down onto the csv file
                writer.writerow([item.get_name(), item.get_category(), item.get_perishable(),
                                 item.get_stock(), item.get_sell_price()])