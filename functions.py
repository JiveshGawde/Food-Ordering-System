from menu import menu

# Function to display menu for a specific category or all categories
def display_menu(category=None):
    try:
        if category:
            if category in menu:
                print(f"\n{category.upper()} MENU:")
                for subcategory, items in menu[category].items():
                    print(f"\n{subcategory.upper()}:")
                    for item, details in items.items():
                        price = details.get('price')
                        ingredients = details.get('ingredients', [])
                        prep_time = details.get('preparation_time')
                        print(f"{item} - ₹{price} | Ingredients: {', '.join(ingredients) if ingredients else 'No ingredients listed'} | Preparation Time: {prep_time} mins")
            else:
                print("Invalid category.")
        else:
            print("\nCATEGORIES:")
            for cat in menu.keys():
                print(f"- {cat.capitalize()}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to get and validate category input
def get_category():
    while True:
        category = input("\nChoose a category (rice, starters, beverages) or type 'done' to finish: ").strip().lower()
        if category == 'done':
            print("\nThank you, please visit again!")
            return category
        if category not in menu:
            print("Invalid category! Try again.")
        else:
            return category

# Function to get and validate subcategory input
def get_subcategory(category):
    while True:
        subcategory = input("\nChoose type (veg/non-veg for rice/starters, hot/cold for beverages) or type 'quit' to exit: ").strip().lower()
        if subcategory == 'quit':
            print("Exiting the process.")
            return None
        if subcategory not in menu[category]:
            print("Invalid choice! Try again.")
        else:
            return subcategory

# Function to get and validate item choice
def get_item_choice(category, subcategory):
    while True:
        item_choice = input("\nEnter item name or type 'quit' to exit: ").strip()
        if item_choice == 'quit':
            print("Exiting the process.")
            return None
        if item_choice not in menu[category][subcategory]:
            print("Invalid item! Try again.")
        else:
            return item_choice

# Function to get and validate quantity
def get_quantity(item_choice):
    while True:
        try:
            quantity_input = input(f"How many {item_choice} do you want? (or type 'quit' to exit): ")
            if quantity_input.lower() == 'quit':
                print("Exiting the process.")
                return None
            quantity = int(quantity_input)
            if quantity <= 0:
                print("Please enter a valid quantity (greater than 0).")
            else:
                return quantity
        except ValueError:
            print("Invalid input! Please enter a valid number for quantity.")

# Function to get spice level for rice/starters
def get_spice_level(category, subcategory, item_choice):
    if category in ["rice", "starters"]:
        available_spice = menu[category][subcategory][item_choice]["spice_level"]
        if len(available_spice) == 1:
            spice = available_spice[0]
            print(f"Only one spice level available: {spice}. Defaulting to {spice}.")
        else:
            while True:
                spice_input = input(f"\nSpice levels available: {', '.join(available_spice)}\nChoose spice level for {item_choice} (or type 'quit' to exit): ").strip().capitalize()
                if spice_input == 'quit':
                    print("Exiting the process.")
                    return None
                if spice_input in available_spice:
                    return spice_input
                else:
                    print("Invalid / Unavailable spice level! Please choose a valid spice level.")
    else:
        return None

def handle_order(category, subcategory):
    """Function to handle an individual item order."""
    cart_item = []

    # Choose the item
    item_choice = get_item_choice(category, subcategory)
    if item_choice is None:
        return cart_item

    # Get quantity
    quantity = get_quantity(item_choice)
    if quantity is None:
        return cart_item
    
    # Get spice level (if applicable)
    spice = get_spice_level(category, subcategory, item_choice)
    
    # Add item to cart
    cart_item.append({
        "item": item_choice, 
        "quantity": quantity, 
        "price": menu[category][subcategory][item_choice]["price"], 
        "spice": spice, 
        "ingredients": menu[category][subcategory][item_choice]["ingredients"]
    })
    
    return cart_item


def print_bill(cart):
    """Function to print the final order and total bill."""
    print("\nYour Final Order:")
    print("-" * 30)
    total = 0
    for item in cart:
        try:
            cost = item["quantity"] * item["price"]
            total += cost
            print(f"{item['item']} x {item['quantity']} - ₹{cost} {'(Spice: ' + item['spice'] + ')' if item['spice'] else ''}")
            print(f"Ingredients: {', '.join(item['ingredients'])}")
            print("-" * 30)
        except KeyError as e:
            print(f"Error processing item: Missing key {e}")
        except Exception as e:
            print(f"Unexpected error processing item: {e}")
    
    try:
        print(f"\nTotal Bill: ₹{total}")
    except Exception as e:
        print(f"Error calculating total bill: {e}")
    
    print("\nThank you for your order!")
