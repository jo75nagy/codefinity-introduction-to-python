grocery_inventory = {"Milk": ("Dairy",3.50,8),
                     "Eggs": ("Dairy",5.50,30),
                     "Bread": ("Bakery",2.99,15),
                     "Apples":("Produce",1.50,50)
                    }
price_of_eggs_tuple = grocery_inventory.get("Eggs")
price_of_eggs = price_of_eggs_tuple[1]
if price_of_eggs > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    new_price_of_eggs = price_of_eggs -1
    grocery_inventory["Eggs"] = (price_of_eggs_tuple[0], 
                                 new_price_of_eggs,
                                 price_of_eggs_tuple[2])
else:
    print("The price of eggs are reasonable.")
grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print("Inventory after adding Tomatoes:",grocery_inventory)

stock_Milk_tuple = grocery_inventory.get("Milk")
stock_of_milk = stock_Milk_tuple[2]
if stock_of_milk < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    new_stock_of_milk = stock_of_milk + 20
    grocery_inventory["Milk"] = ( stock_Milk_tuple[0],
                                   stock_Milk_tuple[1],
                                   new_stock_of_milk)
else:
    print("Milk das sufficient stock.")
price_of_apples_tuple = grocery_inventory.get("Apples")
price_of_apples = price_of_apples_tuple[1]

if price_of_apples > 2.0:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
print("Updated inventory:",grocery_inventory)
    