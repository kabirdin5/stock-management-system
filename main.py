from item import Item
from item_manager import ItemManager

item_manager = ItemManager()

item1 = Item("Bright Striped Strappy Midi", "SundressClothing",
             False,66, 6.72)
item2 = Item("Green Textured Frill Sleeve Midi", "DressClothing",
             False,50, 4.60)
item3 = Item("Khaki Striped Knitted Jumper", "Clothing",
             False, 7, 7.22)
item4 = Item("Sesame Street Black Cookie Monster Graphic T-Shirt", "Clothing",
             False,85, 7.15)
item5 = Item("Blue Wash Turn Up Denim Shorts", "Clothing",
             False,58, 4.15)
item6 = Item("Vegan Creamy Garlic Mushroom", "SliceGrocery - Chilled",
             True,93, 0.40)
item7 = Item("Fat Free Banana and Custard Yogurt", "Grocery - Chilled",
             True,13, 5.19)
item8 = Item("Chicago Town BBQ Crust Deep Dish Memphis Style BBQ Pork", "Grocery - Frozen",
             True,24, 3.14)
item9 = Item("4 Frozen Baked Jacket Potatoes", "Grocery - Frozen",
             True, 47, 7.36)
item10 = Item("Crispy Sweet Potato Fries", "Grocery - Frozen",
              True, 98, 2.99)
item11 = Item("Harry Potter and the Order of the Phoenix by J. K. Rowling", "Books - Paperback",
              False, 62, 9.13)
item12 = Item("We're Going on a Ghost Hunt by Martha Mumford", "Books - Paperback",
              False, 79, 3.59)
item13 = Item("There's a Dinosaur in Your Book by Tom Fletcher", "Books - Paperback",
              False, 60, 0.59)
item14 = Item("Whittiers by Danielle Steel", "Books - Paperback",
              False,  63, 4.03)
item15 = Item("Zog by Julia Donaldson", "Books - Paperback",
              False, 19, 9.32)
new_item3 = Item("Khaki Striped Knitted Jumper", "Clothing",
             False, 7, 7.99)

item_manager.add_item(item1)
item_manager.add_item(item2)
item_manager.add_item(item3)
item_manager.add_item(item4)
item_manager.add_item(item5)
item_manager.add_item(item6)
item_manager.add_item(item7)
item_manager.add_item(item8)
item_manager.add_item(item9)
item_manager.add_item(item10)
item_manager.add_item(item11)
item_manager.add_item(item12)
item_manager.add_item(item13)
item_manager.add_item(item14)
item_manager.add_item(item15)




itemsManager = item_manager.list_items()


"""
item_manager.edit_item(item3, new_item3)
print(itemsManager)
"""


"""
categorised_items = item_manager.search_by_category("Clothing")

for item in categorised_items:
    print(item)
"""


"""
perishable_items = item_manager.search_by_perishable(False)

for item in perishable_items:
    print(item)
"""


"""
searched_price = item_manager.search_by_sell_price(4.03)

for item in searched_price:
    print(item)
"""


"""
x = ["Sesame Street Black Cookie Monster Graphic T-Shirt", "Vegan Creamy Garlic Mushroom", "Fat Free Banana and Custard Yogurt"]
items_to_discount = item_manager.apply_discount_to_items(x, 10)

for item in items_to_discount:
    print(item)
"""




basket = [item1, item2, item3]
total = item_manager.purchase_available_items([item1, item2, item3], True)
if total:
    for item in total:
        print(item)
