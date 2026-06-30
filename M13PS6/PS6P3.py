# This stores last names and scores.
# It finds the highest score and lowest score without using built in methods.

def display_highest_lowest(names, scores):
    high_score = 0
    high_index = 0

    low_score = 999
    low_index = 0

    for i in range(len(scores)):
        if scores[i] > high_score:
            high_score = scores[i]
            high_index = i

        if scores[i] < low_score:
            low_score = scores[i]
            low_index = i

    print("Highest Score:")
    print(names[high_index], high_score)

    print("\nLowest Score:")
    print(names[low_index], low_score)


# Main program
last_names = [
    "Parrish",
    "Blackwell",
    "Todd",
    "Brown",
    "Jones",
    "Garcia",
    "Sawyer",
    "Davis",
    "Miller",
    "Davis"
]

scores = [24, 95, 38, 59, 50, 87, 96, 92, 81, 99]

display_highest_lowest(last_names, scores)
