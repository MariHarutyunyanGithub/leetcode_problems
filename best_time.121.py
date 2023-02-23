# You are given an array prices where prices[i] is the price of a given stock on 
# the ith day. You want to maximize your profit by choosing a single day to buy 
# one stock and choosing a different day in the future to sell that stock. Return 
# the maximum profit you can achieve from this transaction. If you cannot achieve 
# any profit, return 0.

def best_time(prices):
    max_profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        cur_profit = prices[i] - min_price
        max_profit = max(cur_profit, max_profit)
    return max_profit

ls = [7,2,5,3,8,4]
print(best_time(ls))