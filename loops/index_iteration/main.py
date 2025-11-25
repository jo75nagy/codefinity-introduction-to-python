prices = [29.99, 45.50, 12.75, 38.20]
#discounts [10%, 20%, 1.15%, 5% ]
discounts = [0.1, 0.2, 0.15, 0.05]

for index in range(len(prices)):
    prices[index] = prices[index] * (1 - discounts[index])    
    print(f"Updated price for item {index}: ${prices[index]:.2f}")
