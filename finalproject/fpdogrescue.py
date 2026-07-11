# Dog Rescue Application
# This lets the user add dogs, view dogs, find a dog, and quit.

# This list will store all of the dog information.
# Each dog will be stored as a small list inside this bigger list.
dogs = []


def main():
    # This function starts the program by calling the menu.
    menu()


def menu():
    # This loop keeps showing the menu until the user chooses to quit.
    while True:
        print("\nDog Rescue")
        print("----------")
        print("\n\t1. Add a Dog")
        print("\t2. View Dogs")
        print("\t3. Find Dog")
        print("\t4. Quit")

        choice = input("\nSelect a choice: ")

        if choice == "1":
            addDog()
        elif choice == "2":
            viewDogs()
        elif choice == "3":
            findDog()
        elif choice == "4":
            print("\nGoodbye")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")


def addDog():
    # This function asks the user for dog information.
    print("\nAdd a Dog")

    dogName = input("Dog Name: ")
    dogBreed = input("Dog Breed: ")
    dogAge = input("Age: ")
    dogWeight = input("Weight: ")

    # Store one dog as a list.
    dog = [dogName, dogBreed, dogAge, dogWeight]

    # Add the dog to the main dogs list.
    dogs.append(dog)

    print("\nDog has been added.")


def viewDogs():
    # This function displays all dogs that were entered.
    print("\nRescue Dogs")

    if len(dogs) == 0:
        print("No dogs have been added yet.")
    else:
        print("-" * 70)
        print(f"{'Dog':<20}{'Breed':<30}{'Age':<10}{'Weight':<10}")
        print("-" * 70)

        # This for loop goes through each dog in the list.
        for dog in dogs:
            print(f"{dog[0]:<20}{dog[1]:<30}{dog[2]:<10}{dog[3]:<10}")


def findDog():
    # This function searches for a dog by name.
    searchName = input("\nEnter dog name to search: ")

    found = False

    # This for loop checks each dog in the list.
    for dog in dogs:
        if dog[0].lower() == searchName.lower():
            print("\nFound", dog[0])
            print("Breed:", dog[1])
            print("Age:", dog[2])
            print("Weight:", dog[3])
            found = True
            break

    if found == False:
        print("\nSorry, unable to find", searchName)


# This line starts the program.
main()
