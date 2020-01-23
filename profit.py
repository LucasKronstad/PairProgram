def calcprofit(x):
    result = x["sell_price"] * x["inventory"] - (x["cost_price"] * x["inventory"])
    return result

profit = {
  "cost_price": 20,
  "sell_price": 45,
  "inventory": 20
}

print(calcprofit(profit))