# Calculate batting average using a function.

def compute_batting_average(hits, at_bats):
    average = hits / at_bats
    return average


player_count = 0
choice = "yes"

while choice.lower() == "yes":
    last_name = input("Enter player's last name: ")
    hits = float(input("Enter number of hits: "))
    at_bats = float(input("Enter number of at bats: "))

    batting_average = compute_batting_average(hits, at_bats)

    player_count = player_count + 1

    print("Last Name:", last_name)
    print("Batting Average:", format(batting_average, ".3f"))

    choice = input("Do you want to enter another player? yes or no: ")

print("Number of players entered:", player_count)
