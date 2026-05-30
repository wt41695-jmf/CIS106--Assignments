last_name = input("Enter Last Name: ")

midterm = float(input("Enter Midterm Score: "))

final_exam = float(input("Enter Final Exam Score: "))

total_points = (midterm * 0.40) + (final_exam * 0.60)

print("Student:", last_name)
print("Total Exam Points:", format(total_points, ".2f"))
