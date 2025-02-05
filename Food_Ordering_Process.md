
## Create a menu to help user order food
##Step 1: prompt user what they want to eat rice, beverages or starters
##Step 2: prompt user whether they want veg or non veg if starter or rice, cold or hot if beverages
    ##show them the list of items tailored to their choice, for beverages directly jump to Step 4
##Step 3: prompt user whether they want it spicy, medium or mild if starter or rice (note some rice/starters cannnot get above medium)
    ##If user choose an item which can get only medium state that it cannot get more spicy
    ##If user choose to make spicy --> medium or mild make sure it change when added to cart 
##Step 4: prompt user for quantity
    ##Make sure to multiple x(n) price for all with the quantity(n) user wants
    ##Make sure to multiple x(n) the peices in starters with the quantity(n) user wants
##Step 5: Extras
    ##Add to cart at this step
    ##Prompt user with other dish recommendations
        ##If user chooses add that item and get back to step 4
        ##If user does not do next
    ##Prompt user to take extra toppings
        ##Toppings are not added initially if user choose the toppings which goes with the dish then choose price with toppings
##Step 5: prompt user for reorder go back to step 1
    ##If user done ordering generate a list of food items with quantity and price
    ##prompt user to purchase coupons
        ##if chooses add price of coupons to bill and substract the discount
        ##add the record to customer data
        ##complete the order



