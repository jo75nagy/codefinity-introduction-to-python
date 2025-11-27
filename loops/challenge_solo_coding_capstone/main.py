# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
for item_name in inventory:  # item_name -> ("Az elsö elem a sorban utäna egy (:) itt "Bread": !! ")
    current_stock,reg_price,discounted_price = inventory[item_name] # adatot a feldolgozásra kivenni [.., ..  ]
    
    if current_stock < 30:
        print(f"{item_name} need restocking.")
    elif current_stock > 100:
        print(f"{item_name} should be sold at the discounted price of {discounted_price}.") # elöhivashoz: { Var}
    elif current_stock >= 30 and current_stock <= 100:
        print(f"{item_name} should be sold at the regular price of {reg_price}.")


              