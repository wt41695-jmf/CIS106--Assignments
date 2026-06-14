# This reads employee names and salaries from a file,
# calculates bonuses, and displays the total bonuses paid.

# Open the employee file
file = open("employees.txt", "r")

# Initialize total bonus
total_bonus = 0

# Read first employee name
lastname = file.readline().strip()

# Continue until end of file
while lastname != "":

    # Read employee salary
    salary = float(file.readline())

    # Determine bonus rate
    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    # Calculate bonus
    bonus = salary * rate

    # Display employee information
    print("Last Name:", lastname)
    print("Salary:", salary)
    print("Bonus:", bonus)
    print()

    # Add bonus to total
    total_bonus = total_bonus + bonus

    # Read next employee name
    lastname = file.readline().strip()

# Display total bonuses paid
print("Total Bonuses Paid:", total_bonus)

# Close file
file.close()
