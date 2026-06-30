# This stores each student with a list of three grades.
# It calculates each student's average.
# It also calculates the class average for each grade.

def student_averages(students):
    print("Student\t\tAverage")
    print("----------------------")

    for name in students:
        grades = students[name]
        average = (grades[0] + grades[1] + grades[2]) / 3
        print(name, "\t\t", round(average, 2))


def class_grade_averages(students):
    total_grade1 = 0
    total_grade2 = 0
    total_grade3 = 0

    for name in students:
        grades = students[name]
        total_grade1 = total_grade1 + grades[0]
        total_grade2 = total_grade2 + grades[1]
        total_grade3 = total_grade3 + grades[2]

    number_of_students = len(students)

    avg1 = total_grade1 / number_of_students
    avg2 = total_grade2 / number_of_students
    avg3 = total_grade3 / number_of_students

    print("\nClass Average for Each Grade")
    print("-----------------------------")
    print("Grade 1 Average:", round(avg1, 2))
    print("Grade 2 Average:", round(avg2, 2))
    print("Grade 3 Average:", round(avg3, 2))


# Main program
students = {
    "Parrish": [56, 74, 82],
    "Blackwell": [92, 85, 98],
    "Todd": [92, 83, 76],
    "Brown": [84, 82, 86],
    "Jones": [97, 88, 89],
    "Garcia": [79, 84, 81],
    "Sawyer": [95, 97, 96],
    "Davis": [81, 84, 82],
    "Miller": [65, 89, 86],
    "Martinez": [81, 76, 99]
}

student_averages(students)
class_grade_averages(students)
