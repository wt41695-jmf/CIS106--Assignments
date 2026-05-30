purchase_price = float(input("Enter Purchase Price Per Share: "))

current_price = float(input("Enter Current Stock Price: "))

quantity = float(input("Enter Quantity of Shares: "))

value_change = (current_price - purchase_price) * quantity

print("Value Change: $", format(value_change, ".2f"))
