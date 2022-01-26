import pandas as pd
import numpy as np
import time
import sys

start_time = time.time()
accuracy = 10
data = pd.read_csv(sys.argv[1], sep=",")
data = data[data["price"] >= 0]
data["price"] = np.ceil(data["price"] * accuracy)
data["price"] = data["price"].astype(int)

max_price = 500 * accuracy

matrice = [[0 for i in range(max_price + 1)] for i in range(len(data) + 1)]

prices = data["price"].to_list()
profit = data["profit"].to_list()

for i in range(1, len(data) + 1):
    for j in range(1, max_price + 1):
        if i == 0 or j == 0:
            matrice[i][j] = 0
        elif j >= prices[i - 1]:
            value = (profit[i - 1] * prices[i - 1]) / (100 * accuracy)
            matrice[i][j] = max(value + matrice[i - 1][j - prices[i - 1]], matrice[i - 1][j])
        else:
            matrice[i][j] = matrice[i - 1][j]

best_combination = []
data_dict = data.to_dict('records')
i = len(data)
j = max_price
while i >= 0 and j >= 0:
    value = (data_dict[i - 1]["profit"] * data_dict[i - 1]["price"]) / (100 * accuracy)
    if matrice[i][j] == matrice[i - 1][j - data_dict[i - 1]["price"]] + value:
        best_combination.append(data_dict[i - 1])
        j -= data_dict[i - 1]["price"]

    i -= 1

total_cost = sum([item['price'] / accuracy for item in best_combination])
total_profit = matrice[-1][-1]

best_combination = pd.DataFrame(best_combination)
print(best_combination)
print("\n")
print("Total cost: " + str(round(total_cost, 2)) + "€")
print("Profit: " + str(round(total_profit, 2)) + "€")
print('time spend: ', time.time() - start_time, "seconds")
