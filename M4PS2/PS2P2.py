ticker = input("Enter Stock Ticker Symbol: ")

shares = float(input("Enter Number of Shares: "))

cost_per_share = float(input("Enter Cost Per Share: "))

amount_invested = shares * cost_per_share

print("Ticker Symbol:", ticker)
print("Amount Invested: $", format(amount_invested, ".2f"))
