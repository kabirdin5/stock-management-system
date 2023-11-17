<h1>CSC1034: Case Study 2</h1>

<h2>Kabir Din's stock management and purchasing system</h2>

<p>There are 2 classes that contain numerous methods. Each method has a vital part in this stock 
management system. The 2 classes are called Item and ItemsManager. Their properties are explained below:</p>

<pre>
<h3>Item</h3>
<p>The Item class includes all the characteristics of each item e.g. name, category, perishable, stock, sell_price</p>
<h4>def __init__(self, name, category, perishable, stock, sell_price):</h4>
<p>Initialised the Item object where each parameter must be a specific data type.</p>
<h4>def get_name(self):</h4>
<p>Gets the name of the item</p>
<h4>def get_category(self):</h4>
<p>Gets the category of the item</p>
<h4>def get_perishable(self):</h4>
<p>Gets the perishable value of the item</p>
<h4>def get_stock(self):</h4>
<p>Gets the stock number of the item</p>
<h4>def get_sell_price(self):</h4>
<p>Gets the selling price of the item</p>
<h4>def __str__(self)</h4>
<p>Creates a string representation of the item</p>
<h4>def __repr__(self):</h4>
<p>Creates a more official string representation of the item</p>
<h4>def __eq__(self, other):</h4>
<p>Checks if there are 2 items equal to each other, based on their names</p>
<h4>def __hash__(self):</h4>
<p>Creates a hash value for the item</p>
</pre>

<pre>
<h3>ItemManager</h3>
<p>The ItemManager class includes a collection of Item objects and contains these methods below...</p>
<h4>def __init__(self, items=None):</h4>
<p>Initialises the ItemManager object</p>
<h4>def get_items(self):</h4>
<p>Gets the list of items as an object</p>
<h4>def __str__(self):</h4>
<p>Creates a string representation of the ItemManager</p>
<h4>def __repr__(self):</h4>
<p>Creates a more official representation of the ItemManager</p>
<h4>def add_item(self, item):</h4>
<p>Adds an item to the ItemManager</p>
<h4>def remove_item(self, item):</h4>
<p>Removes an item from the ItemManager</p>
<h4>def edit_item(self, old_item, new_item):</h4>
<p>Edits an existing item from ItemManager</p>
<h4>def search_by_category(self, category):</h4>
<p>Searches for the items by category</p>
<h4>def search_by_perishable(self, perishable):</h4>
<p>Searches for the items by their perishable status</p>
<h4>def search_by_sell_price(self, sell_price):</h4>
<p>Searches for the items by their sell_price</p>
<h4>def apply_discount_to_items(self, names, discount):</h4>
<p>Applies the discount to the chosen items from ItemsManager</p>
<h4>def purchase_available_items(self, names, is_member):</h4>
<p>Calculates the total cost for the chosen purchased items and updates the stock.</p>
<h4>def load_from_file(self, file_name):</h4>
<p>Loads the items from the csv file (sample_data.csv)</p>
<h4>def save_to_file(self, file_name):</h4>
<p>Writes the given items to a csv file (testing_data.csv)</p>
</pre>


