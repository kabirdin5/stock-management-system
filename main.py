from item import Item
from item_manager import ItemManager

item_manager = ItemManager()
ItemsManager = item_manager.list_items()

print("Testing Section\n")

item1 = Item("Apple", "Fruit", True, 12, 0.85)
item2 = Item("Dragon Fruit", "Fruit", True, 8, 1.29)
item3 = Item("Carrot", "Vegetable", True, 12, 1.19)
item4 = Item("Plain black t-shirt", "Clothing", False, 16, 12.99)

print("These are the items that we will be using in testing:")
print(item1)
print(item2)
print(item3)
print(item4)
print("\nEach item variable contains the values: \n(name, category, perishable, stock, price)")
print("\nWe will go through the different methods to test if they work according to specification...")


def test_get_name():
    print("Test Case: get_name()")
    try:
        print("Name of item1: " + Item.get_name(item1))
        print("Name of item2: " + Item.get_name(item2))
        print("Name of item3: " + Item.get_name(item3))
        print("Name of item4: " + Item.get_name(item4))
    except:
        print("Failed unexpectedly")

def test_fail_get_name():
    print("\nTest Case: Failed get_name()")
    try:
        # Testing an undefined item
        print("Name of item5: " + Item.get_name(item5))
        # Testing with a non-string attribute
        item5 = Item(10, "Clothing", False,
                      14, 11.99)
        print("Name of item5: " + Item.get_name(item5))
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test_get_category():
    print("\nTest Case: get_category()")
    try:
        print("Category of item1: " + Item.get_category(item1))
        print("Category of item2: " + Item.get_category(item1))
        print("Category of item3: " + Item.get_category(item1))
        print("Category of item4: " + Item.get_category(item1))
    except:
        print("Failed unexpectedly")

def test_fail_get_category():
    print("\nTest Case: Failed get_category()")
    try:
        # Testing an undefined item
        print("Category of item5: " + Item.get_category(item5))
        # Testing with a non-string attribute
        item5 = Item("Plain white t-shirt", 10, False,
                     14, 11.99)
        print("Category of item5: " + Item.get_name(item5))
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test_get_perishable():
    print("\nTest Case: get_perishable()")
    try:
        print(f"Perishable of item1: {Item.get_perishable(item1)} ")
        print(f"Perishable of item2: {Item.get_perishable(item2)} ")
        print(f"Perishable of item3: {Item.get_perishable(item3)} ")
        print(f"Perishable of item4: {Item.get_perishable(item4)} ")
    except:
        print("Failed unexpectedly")

def test_fail_get_perishable():
    print("\nTest Case: Failed get_perishable()")
    try:
        # Testing an undefined item
        print("Perishable of item5: " + Item.get_perishable(item5))
        # Testing with a string instead of a boolean
        item5 = Item("Plain white t-shirt", "Clothing", "False",
                     14, 11.99)
        print("Perishable of item5: " + Item.get_name(item5))
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test_get_stock():
    print("\nTest Case: get_stock()")
    try:
        print(f"Stock of item1: {Item.get_stock(item1)}")
        print(f"Stock of item2: {Item.get_stock(item2)}")
        print(f"Stock of item3: {Item.get_stock(item3)}")
        print(f"Stock of item4: {Item.get_stock(item4)}")
    except:
        print("Failed unexpectedly")

def test_fail_get_stock():
    print("\nTest Case: Failed get_stock()")
    try:
        # Testing an undefined item
        print("Stock of item5: " + Item.get_category(item5))
        # Testing with a string instead of an integer
        item5 = Item("Plain white t-shirt", "Clothing", False,
                     "14", 11.99)
        print("Stock of item5: " + Item.get_name(item5))
        # Testing with a value below 0
        new_item5 = Item("Plain white t-shirt", "Clothing", False,
                    -5, 11.99)
        print("Stock of new_item5: " + Item.get_name(new_item5))
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test_get_sell_price():
    print("\nTest Case: get_sell_price()")
    try:
        print(f"Sell_price of item1: {Item.get_sell_price(item1)}")
        print(f"Sell_price of item2: {Item.get_sell_price(item2)}")
        print(f"Sell_price of item3: {Item.get_sell_price(item3)}")
        print(f"Sell_price of item4: {Item.get_sell_price(item4)}")
    except:
        print("Failed unexpectedly")

def test_fail_get_sell_price():
    print("\nTest Case: Failed get_sell_price()")
    try:
        # Testing an undefined item
        print("Sell_price of item5: " + Item.get_sell_price(item5))
        # Testing with a string instead of an integer
        item5 = Item("Plain white t-shirt", "Clothing", False,
                     14, "11.99")
        print("Sell_price of item5: " + Item.get_sell_price(item5))
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test__str__():
    print("\nTest Case: __str__()")
    try:
        print(f"Item 1 using __str__(): {Item.__str__(item1)}")
        print(f"Item 2 using __str__(): {Item.__str__(item2)}")
        print(f"Item 3 using __str__(): {Item.__str__(item3)}")
        print(f"Item 4 using __str__(): {Item.__str__(item4)}")
    except:
        print("Failed unexpectedly")

def test_fail__str__():
    print("\nTest Case: Failed __str__()")
    try:
        # Testing an undefined item
        print(f"Item 5 using __str__(): {Item.__str__(item5)}")
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test__repr__():
    print("\nTest Case: __repr__()")
    try:
        print(f"Item 1 using __repr__(): {Item.__repr__(item1)}")
        print(f"Item 2 using __repr__(): {Item.__repr__(item2)}")
        print(f"Item 3 using __repr__(): {Item.__repr__(item3)}")
        print(f"Item 4 using __repr__(): {Item.__repr__(item4)}")
    except:
        print("Failed unexpectedly")

def test_fail__repr__():
    print("\nTest Case: Failed __repr__()")
    try:
        # Testing an undefined item
        print(f"Item 5 using __repr__(): {Item.__repr__(item5)}")
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test__eq__():
    print("\nTest Case: __eq__()")
    try:
        # Testing to see if both items have the same name
        item1_1 = item1 = Item("Apple", "Fruit", True, 10, 0.82)
        print(f"item1_1: {item1_1}")
        # Test to expect 'True'
        print(f"Comparing item 1 to item1_1: {Item.__eq__(item1, item1_1)}")
        # Test to expect 'False'
        print(f"Comparing item1 to item2: {Item.__eq__(item1, item2)}")
    except:
        print("Failed unexpectedly")

def test_fail__eq__():
    print("\nTest Case: Failed __eq__()")
    try:
        # Testing to compare a defined item with an undefined item
        print(f"Comparing item1 to item5: {Item.__eq__(item1, item5)}")
        # Testing to compare 3 defined items
        print(f"Comparing item1, item2 and item3 with each other: {Item.__eq__(item1, item2, item3)}")
        # Testing to see if the item compares with itself
        print(f"Comparing item1 with itself: {Item.__eq__(item1)}")
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test__hash__():
    print("\nTest Case: __hash__()")
    try:
        print(f"Item 1 using __hash__(): {Item.__hash__(item1)}")
        print(f"Item 2 using __hash__(): {Item.__hash__(item2)}")
        print(f"Item 3 using __hash__(): {Item.__hash__(item3)}")
        print(f"Item 4 using __hash__(): {Item.__hash__(item4)}")
    except:
        print("Failed unexpectedly")

def test_fail__hash__():
    print("\nTest Case: Failed __hash__()")
    try:
        # Testing an undefined item
        print(f"Item 5 using __hash__(): {Item.__hash__(item5)}")
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test_add_item():
    print("\nTest Case: add_item")
    try:
        item_manager.add_item(item1)
        item_manager.add_item(item2)
        item_manager.add_item(item3)
        item_manager.add_item(item4)
        print(ItemsManager)
    except:
        print("Failed unexpectedly")

def test_fail_add_item():
    print("\nTest Case: Failed add_item")
    try:
        item_manager.add_item(item1)
        item_manager.add_item(item1)
        item_manager.add_item(item3)
        item_manager.add_item(item4)
        # Adding an undefined item
        item_manager.add_item(item5)
        print(ItemsManager)
    except:
        print("Failed expectedly")
    else:
        print("Should have failed")





test_get_name()
test_fail_get_name()
test_get_category()
test_fail_get_category()
test_get_perishable()
test_fail_get_perishable()
test_get_stock()
test_fail_get_stock()
test_get_sell_price()
test_fail_get_sell_price()
test__str__()
test_fail__str__()
test__repr__()
test_fail__repr__()
test__eq__()
test_fail__eq__()
test__hash__()
test_fail__hash__()
test_add_item()
test_fail_add_item()
