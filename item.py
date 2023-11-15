class Item:

    def __init__(self, name, category, perishable, stock, sell_price):
        if not isinstance(name, str):
            raise TypeError("Name of item must be a string")
        self.name = name
        if not isinstance(category, str):
            raise TypeError("Category of item must be a string")
        self.category = category
        if not isinstance(perishable, bool):
            raise TypeError("Perishable of item must be a boolean value")
        self.perishable = perishable
        if not isinstance(stock, int):
            raise TypeError("Stock of item must be an integer")
        self.stock = stock
        if not isinstance(sell_price, float):
            raise TypeError("Selling price of item must be a float")
        self.sell_price = round(sell_price, 2)

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_perishable(self):
        return self.perishable

    def get_stock(self):
        return self.stock

    def get_sell_price(self):
        return self.sell_price

    def __str__(self):
        return "({},{},{},{},{})".format(self.name, self.category, self.perishable,
                                             self.stock, self.sell_price)

    def __repr__(self):
        return str(Item(self.name, self.category, self.perishable, self.stock, self.sell_price))

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.name == other.name
        return False


    def __hash__(self):
        return Item(self.name, self.category, self.perishable, self.stock, self.sell_price)