from menu import menu 

#Function to display the menu
def display_menu(category=None):
    try:
        #checking category
        if category:
            #checking category in the menu
            if category in menu:
                #show category : "Rice Menu:"
                print(f"\n{category.upper()} MENU:")
                #check for subcategory i.e veg/non-veg, hot/cold, items i.e. Fried Rice, Curd Rice...
                for subcategory, items in menu[category].items():
                    #show subcategory : "VEG:"
                    print(f"\n{subcategory.upper()}:")
                    #access to all the details like price and preparation time...
                    for item, details in items.items():
                        #show format : "Fried Rice - ₹100"
                        price = details.get('price')
                        ingredients = details.get('ingredients', [])
                        prep_time = details.get('preparation_time')
                        print(f"{item} - ₹{price} | Ingredients: {', '.join(ingredients) if ingredients else 'No ingredients listed'} | Preparation Time: {prep_time}")

            else:
                #no such category available
                print("Invalid category.")
        else:
            #prints all three categories if we run function as it is display_menu()
            print("\nCATEGORIES:")
            for cat in menu.keys():
                print(f"- {cat.capitalize()}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#Function to take user order
def take_order():
    cart = []
    
    while True:
        display_menu()
        category = input("\nChoose a category (rice, starters, beverages) or type 'done' to finish: ").strip().lower()
        if category == 'done':
            print("\nThank you, please visit again!")
            break
        if category not in menu:
            print("Invalid category! Try again.")
            continue
        
        display_menu(category)
        subcategory = input("\nChoose type (veg/non-veg for rice/starters, hot/cold for beverages): ").strip().lower()
        if subcategory not in menu[category]:
            print("Invalid choice! Try again.")
            continue
        
        print("\nAvailable Items:")
        for item, details in menu[category][subcategory].items():
            print(f"{item} - ₹{details['price']}")

        item_choice = input("\nEnter item name: ").strip()
        if item_choice not in menu[category][subcategory]:
            print("Invalid item! Try again.")
            continue
        
        quantity = int(input(f"How many {item_choice} do you want? "))
        
        #Handling spice level for rice/starters
        if category in ["rice", "starters"]:
            available_spice = menu[category][subcategory][item_choice]["spice_level"]
            
            if len(available_spice) == 1:  
                spice = available_spice[0]
                print(f"Only one spice level available: {spice}. Defaulting to {spice}.")
            else:
                print(f"\nSpice levels available: {', '.join(available_spice)}")
                spice = input(f"Choose spice level for {item_choice}: ").strip().capitalize()
                

                if spice not in available_spice:
                    print("Invalid / Unavailable spice level! Defaulting to Medium.")
                    spice = "Medium"
         #Beverages don't have spice levels
        else:
            spice = None

        
        cart.append({
            "item": item_choice, 
            "quantity": quantity, 
            "price": menu[category][subcategory][item_choice]["price"], 
            "spice": spice, 
            "ingredients": menu[category][subcategory][item_choice]["ingredients"]
            })

        
        another = input("Do you want to add another item? (yes/no): ").strip().lower()
        if another != "yes":
            break

     # Print Final Order and Total Bill after the loop ends (when 'done' is entered)
    if cart:
        print("\nYour Final Order:")
        print("-"* 30, "\n")
        total = 0
        for item in cart:
            cost = item["quantity"] * item["price"]
            total += cost
            print(f"{item['item']} x {item['quantity']} - ₹{cost} {'(Spice: ' + item['spice'] + ')' if item['spice'] else ''} ")
            print(f"Ingredients: {', '.join(item['ingredients'])}")
            print("-"* 30, "\n")
        
        print(f"\nTotal Bill: ₹{total}")
        print("\nThank you for your order!")


# Run ordering system
if __name__ == "__main__":
    take_order()

