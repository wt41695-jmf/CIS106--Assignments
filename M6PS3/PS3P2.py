# Get quantity from user
quantity = int(input("Enter quantity of widgets: "))

# Determine price based on quantity
if quantity > 10000:
    price = 10.00
elif quantity >= 5000:
    price = 20.00
else:
    price = 30.00

# Calculate extended price, tax, and total
extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

# Display results
print(f"Extended Price: ${extended_price:.2f}")
print(f"Tax Amount: ${tax:.2f}")
print(f"Total: ${total:.2f}")
