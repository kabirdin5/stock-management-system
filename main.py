from item import Item
from item_manager import ItemManager

item_manager = ItemManager()
ItemsManager = item_manager.list_items()

print("Testing Section\n")

item1 = Item("Apple", "Fruit", True, 12, 0.85)
item2 = Item("Dragon Fruit", "Fruit", True, 8, 1.29)
item3 = Item("Carrot", "Vegetable", True, 12, 1.29)
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
        # Testing with a number below 0
        item5 = Item("Plain white t-shirt", "Clothing", False,
                     14, -10)
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
    print("\nTest Case: add_item()")
    try:
        item_manager.add_item(item1)
        item_manager.add_item(item2)
        item_manager.add_item(item3)
        item_manager.add_item(item4)
        print(ItemsManager)
    except:
        print("Failed unexpectedly")


def test_fail_add_item():
    print("\nTest Case: Failed add_item()")
    try:
        # Adding an undefined item
        item_manager.add_item(item5)
        print(ItemsManager)
    except:
        print("Failed expectedly")
    else:
        print("Should have failed")


def test_remove_item():
    print("\nTest Case: remove_item()")
    try:
        # All items except item1 has been removed
        # Expected to only print item1.
        item_manager.remove_item(item2)
        item_manager.remove_item(item3)
        item_manager.remove_item(item4)
        print(ItemsManager)
    except:
        print("Failed unexpectedly")


def test_fail_remove_item():
    print("\nTest Case: Failed remove_item()")
    try:
        # Removing an item that has already been removed
        item_manager.remove_item(item3)
        print(ItemsManager)
    except:
        print("Failed expectedly")
    else:
        print("Should have failed")


def test_edit_item():
    print("\nTest Case: edit_item()")
    try:
        new_item1 = Item("Apple", "Fruit", True, 12, 1.15)
        print(f"New_item1: {new_item1}")
        print("This new item has a price increase from £0.85 to £1.15")
        item_manager.add_item(item2)
        item_manager.add_item(item3)
        item_manager.add_item(item4)
        item_manager.edit_item(item1, new_item1)
        print(ItemsManager)
    except:
        print("Failed unexpectedly")


def test_failed_edit_item():
    print("\nTest Case: Failed edit_item()")
    try:
        # Editing item1 with an undefined variable
        item_manager.edit_item(item1, item5)
        print(ItemsManager)
    except:
        print("Failed expectedly")
    else:
        print("Should have failed")


def test_search_by_category():
    print("\nTest Case: search_by_category()")
    try:
        # Expected to print the items in the fruit category
        categorised_items = item_manager.search_by_category("Fruit")
        for item in categorised_items:
            print(item)
    except:
        print("Failed unexpectedly")


def test__failed_search_by_category():
    print("\nTest Case: Failed search_by_category()")
    try:
        # Testing to see if category can be a non-string
        item5 = Item("Blue denim trousers", 10, False, 41, 29.99)
        categorised_items = item_manager.search_by_category(10)
        for item in categorised_items:
            print(item)
    except:
        print("Failed expectedly")
        print("Category of item must be a string")
    else:
        print("Should have failed")


def test_search_by_perishable():
    print("\nTest Case: search_by_perishable()")
    try:
        # Expect to print out the items where the perishable value is True
        perishable_items = item_manager.search_by_perishable(True)
        for item in perishable_items:
            print(item)
    except:
        print("Failed unexpectedly")


def test_failed_search_by_perishable():
    print("\nTest Case: Failed search_by_perishable()")
    try:
        # Testing to see if I am able to use a string instead of a boolean
        item5 = Item("Blue denim trousers", "Clothing", "False", 41, 29.99)
        item_manager.add_item(item5)
        perishable_items = item_manager.search_by_perishable("False")
        for item in perishable_items:
            print(item)
    except:
        print("Failed expectedly")
        print("Perishable of item must be a boolean value")
    else:
        print("Should have failed")


def test_search_by_sell_price():
    print("\nTest Case: search_by_sell_price()")
    try:
        # Expect to print the items with the sell price of £1.29
        searched_price_items = item_manager.search_by_sell_price(1.29)
        for item in searched_price_items:
            print(item)
    except:
        print("Failed unexpectedly")


def test_failed_search_by_sell_price():
    print("\nTest Case: Failed search_by_sell_price()")
    try:
        # Testing to see if I am able to use a string instead of an integer
        item5 = Item("Blue denim trousers", "Clothing", False, 41, "29.99")
        item_manager.add_item(item5)
        search_price_items = item_manager.search_by_perishable("29.99")
        for item in search_price_items:
            print(item)
    except:
        print("Failed expectedly")
        print("Stock of item must be an integer")
    else:
        print("Should have failed")


def test_apply_discount_to_items():
    print("\nTest Case: apply_discount_to_items()")
    try:
        basket = ["Apple", "Carrot"]
        items_to_discount = item_manager.apply_discount_to_items(basket, 10)

        for item in items_to_discount:
            print(item)
    except:
        print("Failed unexpectedly")


def test_failed_apply_discount_to_items():
    print("\nTest Case: Failed apply_discount_to_items()")
    try:
        # Testing to see if the items are discounted outside the range
        basket = ["Apple", "Carrot"]
        items_to_discount = item_manager.apply_discount_to_items(basket, 60)

        for item in items_to_discount:
            print(item)
    except:
        print("Failed expectedly")
    else:
        print("Should have failed")


def test_purchase_available_items():
    print("\nTest Case: purchase_available_items()")
    try:
        basket = ["Apple", "Carrot", "Black t-shirt"]
        total_cost = item_manager.purchase_available_items(basket, True)
        print(round(total_cost, 2))
    except:
        print("Failed unexpectedly")


def test_failed_purchase_available_items():
    print("\nTest Case: Failed purchase_available_items()")
    try:
        # Testing to see if the items are added together when the stock is below 0.
        item5 = Item("Banana", "Fruit", True, -1, 1.42)
        item6 = Item("Grapes", "Fruit", True, -2, 2.19)
        item7 = Item("Tomato", "Vegetable", True, -2, 1.25)
        item_manager.add_item(item5)
        item_manager.add_item(item6)
        item_manager.add_item(item7)
        basket = ["Banana", "Grapes", "Tomato"]
        total_cost = item_manager.purchase_available_items(basket, False)
        print(round(total_cost, 2))
    except:
        print("Failed expectedly")
    else:
        print("Should have failed")


def test_load_from_file():
    print("\nTest Case: load_from_file()")
    try:
        print("Here are the items below that are contained in the sample.csv: ")
        basket = item_manager.load_from_file("sample_data.csv")
        for item in basket:
            print(item)
    except:
        print("Failed unexpectedly")

def test_save_to_file():
    print("\nTest Case: save_to_file()")
    try:
        print("The test items that I have been using will be saved into the testing_data.csv file:")
        print(item1)
        print(item2)
        print(item3)
        print(item4)
        ItemsManager.clear()
        item_manager.add_item(item1)
        item_manager.add_item(item2)
        item_manager.add_item(item3)
        item_manager.add_item(item4)
        item_manager.save_to_file("testing_data.csv")
    except:
        print("Failed unexpectedly")



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
test_remove_item()
test_fail_remove_item()
test_edit_item()
test_failed_edit_item()
test_search_by_category()
test__failed_search_by_category()
test_search_by_perishable()
test_failed_search_by_perishable()
test_search_by_sell_price()
test_failed_search_by_sell_price()
test_apply_discount_to_items()
test_failed_apply_discount_to_items()
test_purchase_available_items()
test_failed_purchase_available_items()
test_load_from_file()
test_save_to_file()