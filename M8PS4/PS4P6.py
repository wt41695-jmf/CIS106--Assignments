# This program calculates the average of two exam scores.
# The user decides whether to continue entering students.

# Ask the user if they want to do the program
answer = input("Do you want to continue? (Yes/No): ")

# Start the student count at zero
count = 0

# Continue looping while the user enters Yes
while answer.lower() == "yes":

    # Prompt for student's last name
    lastname = input("Enter student's last name: ")

    # Prompt for exam scores
    exam1 = float(input("Enter Exam Score 1: "))
    exam2 = float(input("Enter Exam Score 2: "))

    # Calculate average exam score
    average = (exam1 + exam2) / 2

    # Display student's information
    print("Last Name:", lastname)
    print("Average:", average)

    # Increase the number of students entered
    count = count + 1

    # Ask if the user wants to do the loop again
    answer = input("Do you want to continue? (Yes/No): ")

# Display total number of students entered
print("Number of students entered:", count)
