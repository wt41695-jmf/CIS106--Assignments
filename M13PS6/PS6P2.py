# This uses two parallel lists.
# One list stores last names.
# The other list stores exam scores.
# The same index connects the student name to the student's score.

def display_names_scores(names, scores):
    print("Last Name\tScore")
    print("---------------------")
    for i in range(len(names)):
        print(names[i], "\t\t", scores[i])


def display_reverse(names, scores):
    print("\nLast Name\tScore")
    print("---------------------")
    for i in range(len(names) - 1, -1, -1):
        print(names[i], "\t\t", scores[i])


# Main program
last_names = [
    "Parrish",
    "Blackwell",
    "Todd",
    "Brown",
    "Jones",
    "Garcia",
    "Sawyer",
    "Miller",
    "Davis",
    "Rodriguez"
]

exam_scores = [49, 76, 28, 87, 60, 92, 83, 81, 34, 95]

display_names_scores(last_names, exam_scores)
display_reverse(last_names, exam_scores)
