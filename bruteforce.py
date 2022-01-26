import pandas as pd
from itertools import combinations
import sys
import time


start_time = time.time()

data = pd.read_csv(sys.argv[1], sep=",")
data = data[data["price"] >= 0]
data = data.to_dict('records')

max_price = 500

best_profit = 0
cost = 0
best_combination = []
for i in range(1, len(data) + 1):
    for combination in combinations(data, i):
        total_profit = 0
        total_cost = 0
        for action in list(combination):
            total_profit += (action['profit'] * action['price'])/100
            total_cost += action['price']
        if total_cost <= max_price and total_profit > best_profit:
            best_profit = total_profit
            cost = total_cost
            best_combination = list(combination)

best_combination = pd.DataFrame(best_combination)
print(best_combination)
print("\n")
print("Total cost: " + str(round(cost, 2)) + "€")
print("Profit: " + str(round(best_profit, 2)) + "€")
print('time spend: ', time.time() - start_time, "seconds")
