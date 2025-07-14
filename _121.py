prices = [7,6,4,3,1]

max_profit = 0
min_price = prices[0]

i = 0
n = len(prices)

while i < n:
    min_price = min(min_price, prices[i])
    max_profit = max(max_profit, prices[i]-min_price)
    i += 1

print(max_profit)