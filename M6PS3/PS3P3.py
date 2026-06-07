# Get part number and quantity from user
part_number = int(input("Enter part number: "))
quantity = int(input("Enter quantity: "))

# Determine unit cost based on part number
if part_number == 10 or part_number == 55:
    unit_cost = 1.00
elif part_number == 99:
    unit_cost = 2.00
elif part_number == 80 or part_number == 70:
    unit_cost = 3.00
else:
    unit_cost = 5.00

# Calculate total cost
total_cost = quantity * unit_cost

# Display results
print("Part Number:", part_number)
print(f"Unit Cost: ${unit_cost:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
