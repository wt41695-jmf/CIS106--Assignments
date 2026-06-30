# This creates a dictionary.
# The student name is the key.
# The grade is the value.

students = {
    "Parrish": 96,
    "Blackwell": 92,
    "Todd": 85,
    "Brown": 72,
    "Jones": 90,
    "Garcia": 67,
    "Sawyer": 95,
    "Davis": 77,
    "Miller": 85,
    "Martinez": 89
}

total = 0

print("Student\t\tGrade")
print("---------------------")

for name in students:
    print(name, "\t\t", students[name])
    total = total + students[name]

average = total / len(students)

print("\nClass Average:", round(average, 2))
