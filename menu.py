menu = {
    # 20 rice dishes
    "rice": {
        #Veg Rice
        "veg": {
            "Fried Rice": {
                "price": 100,
                "spice_level": ["Mild", "Medium", "Spicy"],
                "preparation_time": 15,
                "ingredients": ["Rice", "Carrots", "Beans", "Capsicum", "Soy Sauce"],
                "add_ons": {"Extra Veggies": 20, "Cheese": 30},
                "recommendations": ["Manchurian", "Spring Rolls"],
            },
            "Paneer Biryani": {
                "price": 160,
                "spice_level": ["Mild", "Medium", "Spicy"],
                "preparation_time": 25,
                "ingredients": ["Basmati Rice", "Paneer", "Mint", "Spices", "Ghee"],
                "add_ons": {"Extra Paneer": 40, "Curd": 20},
                "recommendations": ["Raita", "Dal Tadka"],
            },
            "Vegetable Pulao": {
                "price": 140,
                "spice_level": ["Mild", "Medium"],
                "preparation_time": 20,
                "ingredients": ["Basmati Rice", "Peas", "Carrots", "Potatoes", "Garam Masala"],
                "add_ons": {"Cashews": 30, "Extra Spices": 10},
                "recommendations": ["Dal Fry", "Salad"],
            },
            "Mushroom Fried Rice": {
                "price": 120,
                "spice_level": ["Mild", "Medium", "Spicy"],
                "preparation_time": 18,
                "ingredients": ["Mushrooms", "Garlic", "Rice", "Soy Sauce"],
                "add_ons": {"Extra Mushrooms": 35, "Spring Onions": 15},
                "recommendations": ["Chili Paneer", "Sweet Corn Soup"],
            },
            "Jeera Rice": {
                "price": 90,
                "spice_level": ["Mild"],
                "preparation_time": 12,
                "ingredients": ["Rice", "Cumin Seeds", "Ghee"],
                "add_ons": {"Butter": 20, "Coriander Leaves": 10},
                "recommendations": ["Dal Makhani", "Aloo Gobi"],
            },
            "Coconut Rice": {
                "price": 130,
                "spice_level": ["Mild", "Medium"],
                "preparation_time": 15,
                "ingredients": ["Rice", "Grated Coconut", "Cashews", "Curry Leaves"],
                "add_ons": {"Extra Coconut": 25, "Ghee": 20},
                "recommendations": ["Vegetable Kurma", "Papad"],
            },
            "Curd Rice": {
                "price": 100,
                "spice_level": ["Mild"],
                "preparation_time": 10,
                "ingredients": ["Rice", "Curd", "Mustard Seeds", "Green Chilies"],
                "add_ons": {"Pomegranate": 15, "Cucumber": 10},
                "recommendations": ["Pickle", "Papad"],
            },
            "Lemon Rice": {
                "price": 110,
                "spice_level": ["Mild", "Medium"],
                "preparation_time": 12,
                "ingredients": ["Rice", "Lemon Juice", "Peanuts", "Curry Leaves"],
                "add_ons": {"Extra Lemon": 10, "Green Chilies": 15},
                "recommendations": ["Coconut Chutney", "Medu Vada"],
            },
            "Tomato Rice": {
                "price": 125,
                "spice_level": ["Mild", "Medium"],
                "preparation_time": 14,
                "ingredients": ["Rice", "Tomatoes", "Garlic", "Red Chilies"],
                "add_ons": {"Extra Tomatoes": 15, "Cashews": 25},
                "recommendations": ["Rasam", "Fryums"],
            },
            "Veg Schezwan Rice": {
                "price": 150,
                "spice_level": ["Medium", "Spicy"],
                "preparation_time": 20,
                "ingredients": ["Rice", "Schezwan Sauce", "Capsicum", "Garlic"],
                "add_ons": {"Extra Schezwan Sauce": 20, "Spring Onions": 10},
                "recommendations": ["Chili Paneer", "Manchow Soup"],
            },
        },
        # non veg rice
        "non-veg": {
            "Chicken Biryani": {
                "price": 180,
                "spice_level": ["Mild", "Medium"],
                "preparation_time": 30,
                "ingredients": ["Basmati Rice", "Chicken", "Yogurt", "Spices"],
                "add_ons": {"Extra Chicken": 50, "Boiled Egg": 30},
                "recommendations": ["Raita", "Chicken Fry"],
            },
            "Mutton Biryani": {
                "price": 250,
                "spice_level": ["Mild", "Medium", "Spicy"],
                "preparation_time": 35,
                "ingredients": ["Basmati Rice", "Mutton", "Spices", "Ghee"],
                "add_ons": {"Extra Mutton": 70, "Curd": 20},
                "recommendations": ["Salad", "Mirchi Ka Salan"],
            },
            "Egg Fried Rice": {
                "price": 130,
                "spice_level": ["Mild", "Medium", "Spicy"],
                "preparation_time": 15,
                "ingredients": ["Eggs", "Rice", "Garlic", "Soy Sauce"],
                "add_ons": {"Extra Egg": 25, "Spring Onions": 15},
                "recommendations": ["Chicken Lollipop", "Sweet Corn Soup"],
            },
            "Prawn Fried Rice": {
                "price": 200,
                "spice_level": ["Mild", "Medium", "Spicy"],
                "preparation_time": 22,
                "ingredients": ["Prawns", "Garlic", "Rice", "Soy Sauce"],
                "add_ons": {"Extra Prawns": 60, "Chili Sauce": 20},
                "recommendations": ["Crab Curry", "Garlic Naan"],
            },
            "Fish Biryani": {
                "price": 220,
                "spice_level": ["Mild", "Medium"],
                "preparation_time": 28,
                "ingredients": ["Rice", "Fish", "Spices", "Yogurt"],
                "add_ons": {"Extra Fish": 80, "Lemon": 10},
                "recommendations": ["Fish Fry", "Raita"],
            },
            "Butter Chicken Rice": {
                "price": 190,
                "spice_level": ["Mild", "Medium"],
                "preparation_time": 25,
                "ingredients": ["Rice", "Butter Chicken", "Tomatoes", "Cream"],
                "add_ons": {"Extra Butter Chicken": 70, "Cheese": 30},
                "recommendations": ["Garlic Naan", "Masala Papad"],
            },
            "Keema Rice": {
                "price": 170,
                "spice_level": ["Mild", "Medium"],
                "preparation_time": 20,
                "ingredients": ["Rice", "Minced Meat", "Onions", "Tomatoes"],
                "add_ons": {"Extra Keema": 50, "Boiled Egg": 20},
                "recommendations": ["Roti", "Spicy Pickle"],
            },
            "Tandoori Chicken Rice": {
                "price": 210,
                "spice_level": ["Mild", "Medium", "Spicy"],
                "preparation_time": 30,
                "ingredients": ["Rice", "Tandoori Chicken", "Spices"],
                "add_ons": {"Extra Chicken": 60, "Yogurt": 15},
                "recommendations": ["Raita", "Tandoori Roti"],
            },
        },
    },
    # 20 starter dishes
    "starters": {
        # Veg Starter
        "veg": {
            "Paneer Tikka": {
                "price": 120,
                "spice_level": ["Mild", "Medium", "Spicy"],
                "pieces": 6,
                "preparation_time": 20,
                "ingredients": ["Paneer", "Yogurt", "Spices", "Bell Peppers"],
                "add_ons": {"Extra Paneer": 40, "Mint Chutney": 20},
                "recommendations": ["Tandoori Roti", "Butter Naan"],
            },
            "Veg Spring Rolls": {
                "price": 100,
                "spice_level": ["Mild", "Medium"],
                "pieces": 6,
                "preparation_time": 15,
                "ingredients": ["Cabbage", "Carrot", "Capsicum", "Soy Sauce"],
                "add_ons": {"Extra Rolls": 30, "Sweet Chili Sauce": 15},
                "recommendations": ["Fried Rice", "Hakka Noodles"],
            },
            "Hara Bhara Kebab": {
                "price": 130,
                "spice_level": ["Mild", "Medium"],
                "pieces": 6,
                "preparation_time": 18,
                "ingredients": ["Spinach", "Peas", "Potatoes", "Spices"],
                "add_ons": {"Extra Kebab": 40, "Yogurt Dip": 20},
                "recommendations": ["Mint Chutney", "Masala Chai"],
            },
            "Crispy Corn": {
                "price": 110,
                "spice_level": ["Mild", "Medium", "Spicy"],
                "pieces": 1,
                "preparation_time": 12,
                "ingredients": ["Sweet Corn", "Corn Flour", "Spices"],
                "add_ons": {"Cheese": 25, "Lemon": 10},
                "recommendations": ["Schezwan Sauce", "Cold Coffee"],
            },
            "Dahi Ke Kebab": {
                "price": 150,
                "spice_level": ["Mild"],
                "pieces": 6,
                "preparation_time": 20,
                "ingredients": ["Hung Curd", "Besan", "Spices"],
                "add_ons": {"Extra Kebabs": 50, "Mint Chutney": 20},
                "recommendations": ["Masala Papad", "Cold Lassi"],
            },
            "Cheese Balls": {
                "price": 140,
                "spice_level": ["Mild"],
                "pieces": 6,
                "preparation_time": 15,
                "ingredients": ["Cheese", "Potatoes", "Breadcrumbs"],
                "add_ons": {"Extra Cheese": 40, "Marinara Sauce": 20},
                "recommendations": ["French Fries", "Tomato Soup"],
            },
            "Stuffed Mushrooms": {
                "price": 160,
                "spice_level": ["Mild", "Medium"],
                "pieces": 6,
                "preparation_time": 22,
                "ingredients": ["Mushrooms", "Cheese", "Garlic", "Herbs"],
                "add_ons": {"Extra Mushrooms": 50, "Garlic Butter": 20},
                "recommendations": ["Garlic Bread", "Creamy Soup"],
            },
            "Aloo Tikki": {
                "price": 90,
                "spice_level": ["Mild", "Medium"],
                "pieces": 2,
                "preparation_time": 10,
                "ingredients": ["Potatoes", "Spices", "Breadcrumbs"],
                "add_ons": {"Extra Tikki": 30, "Sweet Chutney": 15},
                "recommendations": ["Chole Bhature", "Masala Chai"],
            },
            "Chili Paneer": {
                "price": 160,
                "spice_level": ["Medium", "Spicy"],
                "pieces": 6,
                "preparation_time": 18,
                "ingredients": ["Paneer", "Capsicum", "Soy Sauce", "Garlic"],
                "add_ons": {"Extra Paneer": 50, "Spring Onions": 20},
                "recommendations": ["Fried Rice", "Hakka Noodles"],
            },
            "Veg Manchurian": {
                "price": 140,
                "spice_level": ["Medium", "Spicy"],
                "pieces": 6,
                "preparation_time": 20,
                "ingredients": ["Cabbage", "Carrot", "Cornflour", "Soy Sauce"],
                "add_ons": {"Extra Manchurian Balls": 50, "Extra Sauce": 20},
                "recommendations": ["Fried Rice", "Hot & Sour Soup"],
            },
        },
        # non veg starters
        "non-veg": {
            "Chicken Wings": {
                "price": 180,
                "spice_level": ["Mild", "Medium"],
                "pieces": 6,
                "preparation_time": 20,
                "ingredients": ["Chicken", "Garlic", "Spices"],
                "add_ons": {"Extra Wings": 60, "Garlic Dip": 25},
                "recommendations": ["French Fries", "Coleslaw"],
            },
            "Tandoori Chicken": {
                "price": 200,
                "spice_level": ["Mild", "Medium", "Spicy"],
                "pieces": 4,
                "preparation_time": 30,
                "ingredients": ["Chicken", "Yogurt", "Spices"],
                "add_ons": {"Extra Leg Piece": 80, "Mint Chutney": 20},
                "recommendations": ["Butter Naan", "Mutton Rogan Josh"],
            },
            "Mutton Seekh Kebab": {
                "price": 220,
                "spice_level": ["Mild", "Medium", "Spicy"],
                "pieces": 4,
                "preparation_time": 25,
                "ingredients": ["Mutton Mince", "Spices", "Ginger-Garlic"],
                "add_ons": {"Extra Kebab": 70, "Lemon": 15},
                "recommendations": ["Roomali Roti", "Mutton Biryani"],
            },
            "Fish Tikka": {
                "price": 210,
                "spice_level": ["Mild", "Medium"],
                "pieces": 6,
                "preparation_time": 22,
                "ingredients": ["Fish Fillet", "Yogurt", "Spices"],
                "add_ons": {"Extra Fish": 80, "Mint Chutney": 20},
                "recommendations": ["Garlic Naan", "Dal Tadka"],
            },
            "Egg Devil": {
                "price": 140,
                "spice_level": ["Medium"],
                "pieces": 4,
                "preparation_time": 15,
                "ingredients": ["Boiled Egg", "Potato", "Spices"],
                "add_ons": {"Extra Egg": 30, "Tomato Sauce": 15},
                "recommendations": ["Tea", "Paratha"],
            },
            "Chicken 65": {
                "price": 190,
                "spice_level": ["Spicy"],
                "pieces": 6,
                "preparation_time": 18,
                "ingredients": ["Chicken", "Chili Powder", "Yogurt"],
                "add_ons": {"Extra Chicken": 60, "Lemon": 10},
                "recommendations": ["Schezwan Sauce", "Butter Naan"],
            },
        },
    },
    # 20 beverages
    "beverages": {
        #hot beverages
        "hot": {
            "Tea": {
                "price": 50,
                "preparation_time": 5,
                "ingredients": ["Tea Leaves", "Milk", "Water", "Sugar"],
                "add_ons": {"Extra Sugar": 5, "Ginger": 10, "Masala": 15},
                "recommendations": ["Samosa", "Biscuits"],
            },
            "Coffee": {
                "price": 70,
                "preparation_time": 7,
                "ingredients": ["Coffee Powder", "Milk", "Water", "Sugar"],
                "add_ons": {"Extra Coffee Shot": 20, "Whipped Cream": 25},
                "recommendations": ["Cookies", "Brownie"],
            },
            "Masala Chai": {
                "price": 60,
                "preparation_time": 6,
                "ingredients": ["Tea Leaves", "Milk", "Spices", "Sugar"],
                "add_ons": {"Extra Spice Mix": 10, "Honey": 15},
                "recommendations": ["Pakoras", "Paratha"],
            },
            "Ginger Tea": {
                "price": 55,
                "preparation_time": 5,
                "ingredients": ["Tea Leaves", "Ginger", "Milk", "Water"],
                "add_ons": {"Lemon": 10, "Honey": 15},
                "recommendations": ["Mathri", "Toast"],
            },
            "Green Tea": {
                "price": 80,
                "preparation_time": 3,
                "ingredients": ["Green Tea Leaves", "Hot Water"],
                "add_ons": {"Lemon": 10, "Honey": 15},
                "recommendations": ["Salad", "Oats Cookies"],
            },
            "Hot Chocolate": {
                "price": 120,
                "preparation_time": 8,
                "ingredients": ["Cocoa Powder", "Milk", "Sugar"],
                "add_ons": {"Marshmallows": 30, "Cinnamon": 20},
                "recommendations": ["Brownie", "Waffles"],
            },
            "Turmeric Latte": {
                "price": 90,
                "preparation_time": 7,
                "ingredients": ["Milk", "Turmeric", "Honey", "Black Pepper"],
                "add_ons": {"Almond Milk": 20, "Cinnamon": 15},
                "recommendations": ["Energy Bar", "Dry Fruits"],
            },
            "South Indian Filter Coffee": {
                "price": 100,
                "preparation_time": 8,
                "ingredients": ["Filter Coffee", "Milk", "Sugar"],
                "add_ons": {"Extra Coffee Decoction": 25, "Jaggery": 20},
                "recommendations": ["Idli", "Dosa"],
            },
            "Espresso": {
                "price": 90,
                "preparation_time": 5,
                "ingredients": ["Espresso Coffee Beans", "Water"],
                "add_ons": {"Extra Shot": 40, "Whipped Cream": 30},
                "recommendations": ["Croissant", "Dark Chocolate"],
            },
            "Hot Lemon Water": {
                "price": 50,
                "preparation_time": 3,
                "ingredients": ["Lemon", "Hot Water", "Honey"],
                "add_ons": {"Ginger": 10, "Cinnamon": 15},
                "recommendations": ["Fruit Bowl", "Whole Wheat Toast"],
            },
        },
        #cold beverages
        "cold": {
            "Lemonade": {
                "price": 60,
                "preparation_time": 5,
                "ingredients": ["Lemon", "Water", "Sugar", "Mint"],
                "add_ons": {"Extra Lemon": 10, "Soda": 15},
                "recommendations": ["French Fries", "Grilled Sandwich"],
            },
            "Cold Coffee": {
                "price": 90,
                "preparation_time": 8,
                "ingredients": ["Coffee", "Milk", "Ice Cubes", "Sugar"],
                "add_ons": {"Chocolate Syrup": 25, "Whipped Cream": 30},
                "recommendations": ["Brownie", "Chocolate Muffin"],
            },
            "Mango Smoothie": {
                "price": 110,
                "preparation_time": 7,
                "ingredients": ["Mango", "Yogurt", "Honey", "Ice"],
                "add_ons": {"Chia Seeds": 20, "Almonds": 25},
                "recommendations": ["Granola Bar", "Oatmeal"],
            },
            "Strawberry Milkshake": {
                "price": 120,
                "preparation_time": 8,
                "ingredients": ["Strawberries", "Milk", "Ice Cream"],
                "add_ons": {"Whipped Cream": 30, "Chocolate Chips": 25},
                "recommendations": ["Donuts", "Pancakes"],
            },
            "Iced Tea": {
                "price": 80,
                "preparation_time": 5,
                "ingredients": ["Tea", "Lemon", "Ice Cubes"],
                "add_ons": {"Peach Flavor": 20, "Mint": 10},
                "recommendations": ["Salad", "Nachos"],
            },
            "Blue Lagoon": {
                "price": 100,
                "preparation_time": 6,
                "ingredients": ["Blue Curacao", "Lemon", "Soda"],
                "add_ons": {"Extra Mint": 10, "Lemon Slice": 15},
                "recommendations": ["Garlic Bread", "Grilled Chicken"],
            },
            "Chocolate Shake": {
                "price": 130,
                "preparation_time": 8,
                "ingredients": ["Chocolate", "Milk", "Ice Cream"],
                "add_ons": {"Oreo Crumbs": 25, "Whipped Cream": 30},
                "recommendations": ["Chocolate Brownie", "Choco Lava Cake"],
            },
            "Watermelon Juice": {
                "price": 70,
                "preparation_time": 5,
                "ingredients": ["Watermelon", "Mint", "Lemon"],
                "add_ons": {"Basil Seeds": 20, "Ginger": 15},
                "recommendations": ["Grilled Veg Sandwich", "Hummus Platter"],
            },
            "Mojito": {
                "price": 100,
                "preparation_time": 6,
                "ingredients": ["Mint", "Lemon", "Soda", "Sugar"],
                "add_ons": {"Extra Mint": 10, "Basil": 15},
                "recommendations": ["Nachos", "Tacos"],
            },
            "Buttermilk (Chaas)": {
                "price": 50,
                "preparation_time": 4,
                "ingredients": ["Curd", "Water", "Salt", "Spices"],
                "add_ons": {"Jeera (Cumin)": 10, "Mint": 10},
                "recommendations": ["Paratha", "Curry Rice"],
            },
        },
    }
    
}


