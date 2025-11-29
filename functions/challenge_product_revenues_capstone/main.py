# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

#inventory = []
#for prod,price,qty in zip(products,prices,quantities_sold):
#   revenue = price * qty
#    inventory.append((prod,price,qty,revenue))

#revenue_p_product = [(prod,price * qty) for prod,price,qty,revenue in inventory]

#for prod, rev in sorted(revenue_p_product):
#    print(f"{prod} has total revenue of ${rev}")
# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")

def calculate_revenue(prices, quantities_sold):
    list_of_revenues =[]
    for i in range(len(prices)):
        list_of_revenues.append(prices[i] * quantities_sold[i])
    return list_of_revenues
def formatted_output(revenues):
    for prod, rev in sorted(revenues):
        print(f"{prod} has total revenue of ${rev}")

revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products,revenues))
formatted_output(revenue_per_product)
    
    