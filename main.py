from item import Item
from item_manager import ItemManager

"""
All of testing adapted from:
https://ncl.instructure.com/courses/49935/files/7493358?module_item_id=3031874&fd_cookie_set=1
"""

item_manager = ItemManager()
ItemsManager = item_manager.get_items()

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
    print("This test will print the names of the items:")
    try:
        print("Name of item1: " + Item.get_name(item1))
        print("Name of item2: " + Item.get_name(item2))
        print("Name of item3: " + Item.get_name(item3))
        print("Name of item4: " + Item.get_name(item4))
    except:
        print("Failed unexpectedly")


def test_fail_get_name():
    print("\nTest Case: Failed get_name()")
    print("This test includes using an undefined variable and wrong data type to print each item's name.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Testing an undefined item
        print("Name of item5: " + Item.get_name(item5))
        # Testing with a non-string attribute
        item5 = Item(10, "Clothing", False,
                     14, 11.99)
        print("Name of item5: " + Item.get_name(item5))
    except:
        print("Name of item must be a string")
        print("Failed as expected")
    else:
        print("Should have failed")


def test_get_category():
    print("\nTest Case: get_category()")
    print("This test will print the items' categories:")
    try:
        print("Category of item1: " + Item.get_category(item1))
        print("Category of item2: " + Item.get_category(item1))
        print("Category of item3: " + Item.get_category(item1))
        print("Category of item4: " + Item.get_category(item1))
    except:
        print("Failed unexpectedly")


def test_fail_get_category():
    print("\nTest Case: Failed get_category()")
    print("This test includes using an undefined variable and using a non-string attribute to print the categories.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Testing an undefined item
        print("Category of item5: " + Item.get_category(item5))
        # Testing with a non-string attribute
        item5 = Item("Plain white t-shirt", 10, False,
                     14, 11.99)
        print("Category of item5: " + Item.get_name(item5))
    except:
        print("Category of item must be a string")
        print("Failed as expected")
    else:
        print("Should have failed")


def test_get_perishable():
    print("\nTest Case: get_perishable()")
    print("This test will print the perishable status of the items:")
    try:
        print(f"Perishable of item1: {Item.get_perishable(item1)} ")
        print(f"Perishable of item2: {Item.get_perishable(item2)} ")
        print(f"Perishable of item3: {Item.get_perishable(item3)} ")
        print(f"Perishable of item4: {Item.get_perishable(item4)} ")
    except:
        print("Failed unexpectedly")


def test_fail_get_perishable():
    print("\nTest Case: Failed get_perishable()")
    print("This test includes using an undefined variable and using the incorrect data type to print the perishable")
    print("status of each item.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Testing an undefined item
        print("Perishable of item5: " + Item.get_perishable(item5))
        # Testing with a string instead of a boolean
        item5 = Item("Plain white t-shirt", "Clothing", "False",
                     14, 11.99)
        print("Perishable of item5: " + Item.get_name(item5))
    except:
        print("Perishable status of item must be a boolean value")
        print("Failed as expected")
    else:
        print("Should have failed")


def test_get_stock():
    print("\nTest Case: get_stock()")
    print("This test will print the stock amount of each item:")
    try:
        print(f"Stock of item1: {Item.get_stock(item1)}")
        print(f"Stock of item2: {Item.get_stock(item2)}")
        print(f"Stock of item3: {Item.get_stock(item3)}")
        print(f"Stock of item4: {Item.get_stock(item4)}")
    except:
        print("Failed unexpectedly")


def test_fail_get_stock():
    print("\nTest Case: Failed get_stock()")
    print("This test includes using an undefined variable and using the wrong data type to print the stock number of")
    print("each item.")
    print("Of course, this will not work.")
    print("Result:")
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
        print("Stock amount of item must be an integer")
        print("Failed as expected")
    else:
        print("Should have failed")


def test_get_sell_price():
    print("\nTest Case: get_sell_price()")
    print("This test will print out the selling price of each item:")
    try:
        print(f"Sell_price of item1: £{Item.get_sell_price(item1)}")
        print(f"Sell_price of item2: £{Item.get_sell_price(item2)}")
        print(f"Sell_price of item3: £{Item.get_sell_price(item3)}")
        print(f"Sell_price of item4: £{Item.get_sell_price(item4)}")
    except:
        print("Failed unexpectedly")


def test_fail_get_sell_price():
    print("\nTest Case: Failed get_sell_price()")
    print("This test includes using an undefined item and incorrect data type to print the item's selling price.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Testing an undefined item
        print("Sell_price of item5: " + Item.get_sell_price(item5))
        # Testing with a number below 0
        item5 = Item("Plain white t-shirt", "Clothing", False,
                     14, -10)
        print("Sell_price of item5: " + Item.get_sell_price(item5))
    except:
        print("Selling price of item must be a float")
        print("Failed as expected")
    else:
        print("Should have failed")


def test__str__():
    print("\nTest Case: __str__()")
    print("This test will print the string representation of each item:")
    try:
        print(f"Item 1 using __str__(): {Item.__str__(item1)}")
        print(f"Item 2 using __str__(): {Item.__str__(item2)}")
        print(f"Item 3 using __str__(): {Item.__str__(item3)}")
        print(f"Item 4 using __str__(): {Item.__str__(item4)}")
    except:
        print("Failed unexpectedly")


def test_fail__str__():
    print("\nTest Case: Failed __str__()")
    print("This test includes using an undefined item to print the string representation of the item.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Testing an undefined item
        print(f"Item 5 using __str__(): {Item.__str__(item5)}")
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test__repr__():
    print("\nTest Case: __repr__()")
    print("This test will print the more official string representation of each item:")
    try:
        print(f"Item 1 using __repr__(): {Item.__repr__(item1)}")
        print(f"Item 2 using __repr__(): {Item.__repr__(item2)}")
        print(f"Item 3 using __repr__(): {Item.__repr__(item3)}")
        print(f"Item 4 using __repr__(): {Item.__repr__(item4)}")
    except:
        print("Failed unexpectedly")


def test_fail__repr__():
    print("\nTest Case: Failed __repr__()")
    print("This test includes using an undefined item to print the more official string representation of the item.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Testing an undefined item
        print(f"Item 5 using __repr__(): {Item.__repr__(item5)}")
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test__eq__():
    print("\nTest Case: __eq__()")
    print("This test will check if one item is equal to the other.")
    print("This ensures that there are no repeats of items in the ItemManager.")
    print("Only the names of the items are compared with each other.")
    print("If it comes out True, this means that both items have the same name.")
    print("If it comes out False, this means that both items do not have the same name.")
    try:
        # Testing to see if both items have the same name
        item1_1 = Item("Apple", "Fruit", True, 10, 0.82)
        print(f"Here is item1_1: {item1_1}")
        print("This test will compare item1 with item1_1 (expecting True)")
        # Test to expect 'True'
        print(f"Comparing item 1 to item1_1: {Item.__eq__(item1, item1_1)}")
        print("This test will compare item1 with item2 (expecting False)")
        # Test to expect 'False'
        print(f"Comparing item1 to item2: {Item.__eq__(item1, item2)}")
    except:
        print("Failed unexpectedly")


def test_fail__eq__():
    print("\nTest Case: Failed __eq__()")
    print("This test includes comparing with an undefined item,comparing with 3 items simultaneously, and comparing an")
    print("item with itself.")
    print("Of course, this will not work.")
    print("Result:")
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
    print("This test will print the hash representation of each item:")
    try:
        print(f"Item 1 using __hash__(): {Item.__hash__(item1)}")
        print(f"Item 2 using __hash__(): {Item.__hash__(item2)}")
        print(f"Item 3 using __hash__(): {Item.__hash__(item3)}")
        print(f"Item 4 using __hash__(): {Item.__hash__(item4)}")
    except:
        print("Failed unexpectedly")


def test_fail__hash__():
    print("\nTest Case: Failed __hash__()")
    print("This test includes using an undefined item to print the hash representation of the item.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Testing an undefined item
        print(f"Item 5 using __hash__(): {Item.__hash__(item5)}")
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test_add_item():
    print("\nTest Case: add_item()")
    print("This test will add all 4 items into the ItemManager.")
    print("This is what ItemsManager looks like:")
    try:
        ItemsManager.clear()
        item_manager.add_item(item1)
        item_manager.add_item(item2)
        item_manager.add_item(item3)
        item_manager.add_item(item4)
        for item in ItemsManager:
            print(item)
    except:
        print("Failed unexpectedly")


def test_fail_add_item():
    print("\nTest Case: Failed add_item()")
    print("This test includes adding an undefined item to ItemsManager.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Adding an undefined item
        item_manager.add_item(item5)
        print(ItemsManager)
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test_remove_item():
    print("\nTest Case: remove_item()")
    print("This test removes the chosen items from ItemsManager.")
    print("This includes removing item2, item3 and item4.")
    print("Therefore, only item1 will be whats left and printed:")
    try:
        # All items except item1 has been removed
        # Expected to only print item1.
        item_manager.remove_item(item2)
        item_manager.remove_item(item3)
        item_manager.remove_item(item4)
        for item in ItemsManager:
            print(item)
    except:
        print("Failed unexpectedly")


def test_fail_remove_item():
    print("\nTest Case: Failed remove_item()")
    print("This test includes removing an item that has already been removed.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Removing an item that has already been removed
        item_manager.remove_item(item3)
        print(ItemsManager)
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test_edit_item():
    print("\nTest Case: edit_item()")
    print("This test will replace an item to update ItemsManager.")
    try:
        new_item1 = Item("Apple", "Fruit", True, 12, 1.15)
        print(f"New_item1: {new_item1}")
        print("We will be replacing item1 with New_item1")
        print("This new item has a price increase from £0.85 to £1.15")
        print("Here is what ItemsManager looks after editing item1:")
        item_manager.add_item(item2)
        item_manager.add_item(item3)
        item_manager.add_item(item4)
        item_manager.edit_item(item1, new_item1)
        print(ItemsManager)
    except:
        print("Failed unexpectedly")


def test_failed_edit_item():
    print("\nTest Case: Failed edit_item()")
    print("This test includes editing item1 with an undefined item.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Editing item1 with an undefined variable
        item_manager.edit_item(item1, item5)
        print(ItemsManager)
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test_search_by_category():
    print("\nTest Case: search_by_category()")
    print("This test searches the items and print them out by their category.")
    print("The items with the category 'Fruit' are printed below:")
    try:
        # Expected to print the items in the fruit category
        categorised_items = item_manager.search_by_category("Fruit")
        for item in categorised_items:
            print(item)
    except:
        print("Failed unexpectedly")


def test__failed_search_by_category():
    print("\nTest Case: Failed search_by_category()")
    print("This test includes searching the items by their categories.")
    print("However, the category is a non-string attribute.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Testing to see if category can be a non-string
        item5 = Item("Blue denim trousers", 10, False, 41, 29.99)
        categorised_items = item_manager.search_by_category(10)
        for item in categorised_items:
            print(item)
    except:
        print("Category of item must be a string")
        print("Failed as expected")
    else:
        print("Should have failed")


def test_search_by_perishable():
    print("\nTest Case: search_by_perishable()")
    print("This test will search the items and print them by their perishable value.")
    print("The items that have the perishable value 'True' are printed below:")
    try:
        # Expect to print out the items where the perishable value is True
        perishable_items = item_manager.search_by_perishable(True)
        for item in perishable_items:
            print(item)
    except:
        print("Failed unexpectedly")


def test_failed_search_by_perishable():
    print("\nTest Case: Failed search_by_perishable()")
    print("This test includes searching the items by their perishable status.")
    print("However, the value will be a string instead of boolean.")
    print("This is the format being used: 'False'.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Testing to see if I am able to use a string instead of a boolean
        item5 = Item("Blue denim trousers", "Clothing", "False", 41, 29.99)
        item_manager.add_item(item5)
        perishable_items = item_manager.search_by_perishable("False")
        for item in perishable_items:
            print(item)
    except:
        print("Perishable status of item must be a boolean value")
        print("Failed as expected")
    else:
        print("Should have failed")


def test_search_by_sell_price():
    print("\nTest Case: search_by_sell_price()")
    print("This test will search the items by their selling price and printing them.")
    print("The items that cost £1.29 are printed below:")
    try:
        # Expect to print the items with the sell price of £1.29
        searched_price_items = item_manager.search_by_sell_price(1.29)
        for item in searched_price_items:
            print(item)
    except:
        print("Failed unexpectedly")


def test_failed_search_by_sell_price():
    print("\nTest Case: Failed search_by_sell_price()")
    print("This test includes searching the items by their selling price.")
    print("However, the selling price will be a string instead of a float.")
    print("This is the format being used: '29.99'.")
    print("Of course, this will not work.")
    print("Result:")
    try:
        # Testing to see if I am able to use a string instead of an integer
        item5 = Item("Blue denim trousers", "Clothing", False, 41, "29.99")
        item_manager.add_item(item5)
        search_price_items = item_manager.search_by_perishable("29.99")
        for item in search_price_items:
            print(item)
    except:
        print("Selling price of item must be a float")
        print("Failed as expected")

    else:
        print("Should have failed")


def test_apply_discount_to_items():
    print("\nTest Case: apply_discount_to_items()")
    print("This test will apply a given discount to each item in ItemsManager.")
    print("Each item below are given a 10% discount:")
    try:
        basket = ["Apple", "Carrot"]
        items_to_discount = item_manager.apply_discount_to_items(basket, 10)

        for item in items_to_discount:
            print(item)
    except:
        print("Failed unexpectedly")


def test_failed_apply_discount_to_items():
    print("\nTest Case: Failed apply_discount_to_items()")
    print("This test includes applying a discount to each item in ItemsManager.")
    print("However, the given discount is 60% and it restricted to go outside the range 0% - 50%.")
    print("This means that this should be a failed test.")
    print("Here is the result:")
    try:
        # Testing to see if the items are discounted outside the range
        basket = ["Apple", "Carrot"]
        items_to_discount = item_manager.apply_discount_to_items(basket, 60)

        for item in items_to_discount:
            print(item)
    except:
        print("Failed as expected")
    else:
        print("Should have failed")


def test_purchase_available_items():
    print("\nTest Case: purchase_available_items()")
    print("This test gives a total cost of the chosen items from ItemsManager.")
    print("Also, if the user is a member, they are able to get a discount.")
    print("If the original total cost is £50 or more, then the discount will be 10%. Otherwise, it would be 5%.")
    print("Item1, item3 and item4 are included in the basket and the 'is_member' is set to True.")
    print("However, the total cost is below £50 which means that it is only 5% discount.")
    print("Here is the total cost:")
    try:
        basket = ["Apple", "Carrot", "Black t-shirt"]
        total_cost = item_manager.purchase_available_items(basket, True)
        print(f"£{round(total_cost,2)}")
    except:
        print("Failed unexpectedly")


def test_failed_purchase_available_items():
    print("\nTest Case: Failed purchase_available_items()")
    print("This test includes printing out the total cost of the chosen items in ItemsManager.")
    print("Everytime one item is purchased, the stock number decrements by 1.")
    print("This means that if the stock number goes to 0, the item is not longer available to purchase.")
    print("There are more items in ItemsManager that each have a stock number below 0.")
    print("Therefore, I am expecting for this to be a failed test.")
    print("Result:")
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
        print("The stock number is below 0")
        print("Failed as expected")
    else:
        print("Should have failed")


def test_load_from_file():
    print("\nTest Case: load_from_file()")
    print("This test loads and prints the contents of the items from the csv file.")
    print("The filename containing the items is called sample_data.csv")
    try:
        print("Here are the items below that are contained in the file: ")
        basket = item_manager.load_from_file("sample_data.csv")
        for item in basket:
            print(item)
    except:
        print("Failed unexpectedly")


def test_save_to_file():
    print("\nTest Case: save_to_file()")
    print("This test saves the items contained in ItemsManager to a new csv file.")
    print("The file name is testing_data.csv")
    try:
        print("Below is what will be display in the file:")
        print(item1)
        print(item2)
        print(item3)
        print(item4)
        print("To ensure that the test is working correctly, you need to open the testing_data file and should find")
        print("item1, item2, item3 and item4 displayed, included with the headlines.")
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