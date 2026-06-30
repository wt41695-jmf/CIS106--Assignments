# This stores 10 last names in a list.
# One function to display the names normally.
# Another function to display the names in reverse order.

def display_names(names):
    print("Last Names:")
    for i in range(len(names)):
        print(names[i])


def display_reverse(names):
    print("\nLast Names in Reverse Order:")
    for i in range(len(names) - 1, -1, -1):
        print(names[i])


# Main program
last_names = [
    "Parrish",
    "Blackwell",
    "Todd",
    "Brown",
    "Jones",
    "Sawyer",
    "Miller",
    "Davis",
    "Rodriguez",
    "Conrad"
]

display_names(last_names)
display_reverse(last_names)
