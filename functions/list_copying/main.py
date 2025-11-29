def apply_discount(list_of_prices):
    prices_copy = list_of_prices.copy()
    for index in range(len(prices_copy)):
        if prices_copy[index] >2.00:
            prices_copy[index] = prices_copy[index] * 0.9
    return prices_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print(f" Updated product prices: {updated_prices}")