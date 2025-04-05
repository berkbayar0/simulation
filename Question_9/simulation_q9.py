import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

customer_counts = [10, 12, 14, 16, 18]
customer_probs = [0.20, 0.10, 0.30, 0.25, 0.15]

order_sizes = [12, 24, 36, 48]
order_probs = [0.30, 0.40, 0.25, 0.05]

sell_price = 1.4
cost_price = 0.9
leftover_sell_price = 0.7

production_options = [216, 228, 240, 252, 264, 276, 288, 300]
days = 500  

results = []

for production in production_options:
    profits = []
    for _ in range(days):   
        num_customers = np.random.choice(customer_counts, p=customer_probs)

        orders = np.random.choice(order_sizes, size=num_customers, p=order_probs)
        total_demand = np.sum(orders)

        sold_bagels = min(production, total_demand)
        leftover_bagels = max(production - total_demand, 0)

        revenue = (sold_bagels * sell_price) + (leftover_bagels * leftover_sell_price)
        cost = production * cost_price
        profit = revenue - cost
        profits.append(profit)

    avg_profit = np.mean(profits)
    results.append({'Production': production, 'Average Profit': avg_profit})


df_results = pd.DataFrame(results)
print(df_results)

best = df_results[df_results['Average Profit'] == df_results['Average Profit'].max()]
print("\nBest option:")
print(best)

plt.plot(df_results['Production'], df_results['Average Profit'], marker='o')
plt.title("Average Profit by Production Quantity")
plt.xlabel("Bagels Produced")
plt.ylabel("Average Profit (TL)")
plt.grid(True)
plt.show()
