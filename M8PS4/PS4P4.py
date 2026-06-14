# This reads item information from a file
# and calculates extended prices.

# Open the file
file = open("orders.txt", "r")

# Initialize totals
total_extended = 0
count = 0

# Read first item
item = file.readline().strip()

# Loop until end of file
while item != "":

    # Read quantity and price
    quantity = int(file.readline())
    price = float(file.readline())

    # Calculate extended price
    extended = quantity * price

    # Display order information
    print("Item:", item)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Extended Price:", extended)
    print()

    # Update totals
    total_extended += extended
    count += 1

    # Read next item
    item = file.readline().strip()

# Calculate average order
average = total_extended / count

# Display summary information
print("Total Extended Prices:", total_extended)
print("Number of Orders:", count)
print("Average Order:", average)

# Close file
file.close()
