# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 10]
 
list = list(zip(products, prices, quantities_sold))
for index in range(len(list)):
    revenue_p_product = list[index][1] * list[index][2]
    

print(list)
print(revenue_p_product)

# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")