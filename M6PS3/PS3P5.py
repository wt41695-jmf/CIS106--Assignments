# Get number of concert tickets
tickets = int(input("Enter number of concert tickets: "))

# Determine price per ticket
if tickets >= 25:
    price_per_ticket = 50.00
elif tickets >= 10:
    price_per_ticket = 60.00
elif tickets >= 5:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00

# Calculate total cost
total_cost = tickets * price_per_ticket

# Display results
print("Number of Tickets:", tickets)
print(f"Price Per Ticket: ${price_per_ticket:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
