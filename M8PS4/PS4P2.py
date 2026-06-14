# Ask the user for a start, stop, and increment value.
# Display numbers from the start value to the stop value using a while loop.

# Ask the user to enter the starting number
start = int(input("Enter start value: "))

# Ask the user to enter the stopping number
stop = int(input("Enter stop value: "))

# Ask the user to enter the increment number
increment = int(input("Enter increment value: "))

# Keep looping while the start value is less than or equal to the stop value
while start <= stop:

    # Display the current number
    print(start)

    # Add the increment to move to the next number
    start = start + increment
