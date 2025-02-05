from menu import menu
from functions import *

def take_order():
    while True:
        cart = []  # Initialize the cart for each new order
        while True:
            display_menu()
            category = get_category()
            
            if category == 'done':
                print("\nThank you, please visit again!")  # Prints when done
                break

            display_menu(category)
            subcategory = get_subcategory(category)
            if subcategory is None:
                break
            
            
            # Add ordered items to the cart
            cart.extend(handle_order(category, subcategory))

            reorder = input("\nWould you like to place another order? (yes/no): ").strip().lower()
            if reorder != 'yes':
                print("\nThank you, please visit again!")  # Thank the user if they don't want to reorder
                break
        

        # After the ordering loop ends, print the bill
        print_bill(cart)
        exit()



# Run ordering system
if __name__ == "__main__":
    take_order()
