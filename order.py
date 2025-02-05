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
                        print(f"{item} - ₹{price} | Ingredients: {', '.join(ingredients) if ingredients else 'No ingredients listed'} | Preparation Time: {prep_time} mins")

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
        try:
            display_menu()
            category = input("\nChoose a category (rice, starters, beverages) or type 'done' to finish: ").strip().lower()
            
            if category == 'done':
                print("\nThank you, please visit again!")
                break
            
            if category not in menu:
                print("Invalid category! Try again.")
                continue
            
            display_menu(category)
            while True:
                subcategory = input("\nChoose type (veg/non-veg for rice/starters, hot/cold for beverages) or type 'quit' to exit: ").strip().lower()

                if subcategory == 'quit':
                    print("Exiting the process.")
                    return  # Or break if you're within a larger loop, like the overall order process
                elif subcategory not in menu[category]:
                    print("Invalid choice! Try again.")
                    continue  # Ask for the subcategory again if invalid
                break

            print("\nAvailable Items:")
            for item, details in menu[category][subcategory].items():
                print(f"{item} - ₹{details['price']}")

            while True:
                item_choice = input("\nEnter item name or type 'quit' to exit: ").strip()

                if item_choice == 'quit':
                    print("Exiting the process.")
                    return  # Or break if you're within a larger loop, like the overall order process
                elif item_choice not in menu[category][subcategory]:
                    print("Invalid item! Try again.")
                    continue  # Ask for the item choice again if invalid
                break

            # Validate the quantity input (ensure it's a number)
            while True:
                try:
                    quantity_input = input(f"How many {item_choice} do you want? (or type 'quit' to exit): ")
                    if quantity_input.lower() == 'quit':
                        print("Exiting the process.")
                        return  # Or break if you're within a larger loop, like the overall order process
                    quantity = int(quantity_input)
                    if quantity <= 0:
                        print("Please enter a valid quantity (greater than 0).")
                        continue
                    break  # Break out of the loop if the input is valid
                except ValueError:
                    print("Invalid input! Please enter a valid number for quantity.")

            # Handling spice level input for rice/starters
            if category in ["rice", "starters"]:
                available_spice = menu[category][subcategory][item_choice]["spice_level"]
                
                if len(available_spice) == 1:  
                    spice = available_spice[0]
                    print(f"Only one spice level available: {spice}. Defaulting to {spice}.")
                else:
                    # Loop until a valid spice level is selected
                    while True:
                        spice_input = input(f"\nSpice levels available: {', '.join(available_spice)}\nChoose spice level for {item_choice} (or type 'quit' to exit): ").strip().capitalize()
                        
                        if spice_input == 'quit':
                            print("Exiting the process.")
                            return  # Or break if you're within a larger loop, like the overall order process
                        elif spice_input in available_spice:
                            spice = spice_input
                            break  # Exit loop if the spice level is valid
                        else:
                            print("Invalid / Unavailable spice level! Please choose a valid spice level.")

            else:
                spice = None  
  # Beverages don't have spice levels

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
        
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

    # Print Final Order and Total Bill after the loop ends (when 'done' is entered)
    if cart:
        print("\nYour Final Order:")
        print("-" * 30, "\n")
        total = 0
        for item in cart:
            try:
                cost = item["quantity"] * item["price"]
                total += cost
                print(f"{item['item']} x {item['quantity']} - ₹{cost} {'(Spice: ' + item['spice'] + ')' if item['spice'] else ''} ")
                print(f"Ingredients: {', '.join(item['ingredients'])}")
                print("-" * 30, "\n")
            except KeyError as e:
                print(f"Error processing item: Missing key {e}")
            except Exception as e:
                print(f"Unexpected error processing item: {e}")
        
        try:
            print(f"\nTotal Bill: ₹{total}")
        except Exception as e:
            print(f"Error calculating total bill: {e}")
        
        print("\nThank you for your order!")



# Run ordering system
if __name__ == "__main__":
    take_order()

