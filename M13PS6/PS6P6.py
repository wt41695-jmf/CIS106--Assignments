# This loads player names and batting averages from a file.
# It stores them in a dictionary.
# Then it prints the dictionary in two columns.

def load_players():
    players = {}

    file = open("players.txt", "r")

    for line in file:
        data = line.split()
        name = data[0]
        average = data[1]
        players[name] = average

    file.close()

    return players


def display_players(players):
    print("Player Name\tBatting Average")
    print("-------------------------------")

    for name in players:
        print(name, "\t\t", players[name])


# Main program
player_dictionary = load_players()
display_players(player_dictionary)
