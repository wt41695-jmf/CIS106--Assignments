
# Calculate extended prices using a function.

def compute_extended_price(quantity, price):
    # Multiply quantity by price
    total = quantity * price

    # If total is over 10000, apply a 10% discount
    if total > 10000:
        total = total * 0.90

    # Return the final total
    return total


# This variable keeps track of all extended prices
total_extended_price = 0.0

# This controls the loop
choice = "yes"

while choice.lower() == "yes":
    # Ask the user for quantity and price
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price: "))

    # Call the function
    extended_price = compute_extended_price(quantity, price)

    # Add this item's extended price to the grand total
    total_extended_price = total_extended_price + extended_price

    # Display the results for this item
    print("Quantity:", quantity)
    print("Price: $", format(price, ".2f"))
    print("Extended Price: $", format(extended_price, ".2f"))

    # Ask if user wants to continue
    choice = input("Do you want to enter another item? yes or no: ")

# Display the final total after the loop ends
print("Total Extended Price for all items: $", format(total_extended_price, ".2f"))
