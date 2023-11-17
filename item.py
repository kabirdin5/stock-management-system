class Item:
    def __init__(self, name, category, perishable, stock, sell_price):
        """
        Initialises the Item object with these parameters:
        :param name(str): Name of the item
        :param category(str): Category of the item
        :param perishable(bool): Perishable status of the item
        :param stock(int): Stock number of the item
        :param sell_price(float): Selling price of the item
        """
        # Checks if name is a string
        if not isinstance(name, str):
            raise TypeError("Name of item must be a string")
        self.name = name
        # Checks if category is a string
        if not isinstance(category, str):
            raise TypeError("Category of item must be a string")
        self.category = category
        # Checks if perishable is a boolean value
        if not isinstance(perishable, bool):
            raise TypeError("Perishable status of item must be a boolean value")
        self.perishable = perishable
        # Checks if stock is an integer
        if not isinstance(stock, int):
            raise TypeError("Stock amount of item must be an integer")
        self.stock = stock
        # Checks if sell_price is a float
        if not isinstance(sell_price, float):
            raise TypeError("Selling price of item must be a float")
        self.sell_price = round(sell_price, 2)  # Rounds the sell_price to 2 decimal places

    def get_name(self):
        # Gets the name of the item and returns it
        return self.name

    def get_category(self):
        # Gets the category of the item and returns it
        return self.category

    def get_perishable(self):
        # Gets the perishable value of the item and returns it
        return self.perishable

    def get_stock(self):
        # Gets the stock number of the item and returns it
        if self.stock >= 0:  # Ensures the stock number is always equal to or more than 0
            return self.stock

    def get_sell_price(self):
        # Gets the sell_price of the item and returns it
        if self.sell_price >= 0:  # Ensures the sell_price is equal to or more than 0
            return self.sell_price

    """
    Everything I learnt below are from these links:
    - https://ncl.instructure.com/courses/49935/pages/practical-5-dot-1-solutions?module_item_id=3031807
    - https://ncl.instructure.com/courses/49935/pages/practical-6-dot-1-solutions?module_item_id=3031838    
    """

    def __str__(self):
        # Creates a string representation of the item and returns it
        return "({},{},{},{},{})".format(self.name, self.category, self.perishable, self.stock, self.sell_price)

    def __repr__(self):
        # Creates a more official string representation of the item and returns it
        return str(Item(self.name, self.category, self.perishable, self.stock, self.sell_price))

    def __eq__(self, other):
        """
        Checks if there are two items equal to each other, based on their names
        :param other: represents another item to compare
        :return: False if items are not equal, True if items are equal
        """
        if isinstance(other, Item):
            return self.name == other.name
        return False

    def __hash__(self):
        # Creates a hash value for the item and returns it as an integer
        return Item(self.name, self.category, self.perishable, self.stock, self.sell_price)
