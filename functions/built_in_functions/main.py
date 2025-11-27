# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for item_name in products:
    price,quantity_sold = products[item_name]
    
    f_price = float(price)
    i_quantity_sold = int(quantity_sold)
    
    total_sales = f_price * i_quantity_sold
    
    total_sales_list.append(total_sales)
    
    print (f"Total sales for {item_name}: ${total_sales}")

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
print(f"Total sum of all sales: ${total_sum}")
print("Minimum sales: $",min_sales)
print("Maximum sales: $",max_sales)
    