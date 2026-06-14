# This calculates tuition based on district code and credits.

# Open file
file = open("students.txt", "r")

# Initialize totals
total_tuition = 0
student_count = 0

# Read first student name
lastname = file.readline().strip()

# Continue until end of file
while lastname != "":

    # Read district code and credits
    district = file.readline().strip()
    credits = int(file.readline())

    # Determine cost per credit
    if district == "I":
        cost = 250
    else:
        cost = 500

    # Calculate tuition
    tuition = credits * cost

    # Display student information
    print("Student:", lastname)
    print("Credits:", credits)
    print("Tuition Owed:", tuition)
    print()

    # Update totals
    total_tuition += tuition
    student_count += 1

    # Read next student
    lastname = file.readline().strip()

# Display summary
print("Total Tuition Owed:", total_tuition)
print("Number of Students:", student_count)

# Close file
file.close()
