import constants
import random
import sys

Players_copy = constants.PLAYERS
Team_copy = constants.TEAMS
num_players_team = int(len(Players_copy) / len(Team_copy))

#print(len(Players_copy))
def clean():
    for player in Players_copy:
        player['height'] = int(player['height'].split(" ")[0])
        #print(player['height'])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        #print(player['experience'])

def balance_teams():
    available_ids = range(len(constants.PLAYERS))
    panthers_ids = random.sample(available_ids, num_players_team)
    available_ids = [id for id in available_ids if id not in panthers_ids]
    bandits_ids = random.sample(available_ids, num_players_team)
    warriors_ids = available_ids

    global panthers_players, warriors_players, bandits_players
    panthers_players = [constants.PLAYERS[id] for id in panthers_ids]
    bandits_players = [constants.PLAYERS[id] for id in bandits_ids]
    warriors_players = [constants.PLAYERS[id] for id in warriors_ids]
    print("panthers:", panthers_players)
    print("bandits:", bandits_players)
    print("warriors:", warriors_players)

def display_menu():
    print("BASKETBALL TEAM STATS TOOL")
    print("\n\n---- MENU----\n\n")
    print("Here are your choices:")
    print("\tA) Display Team Stats")
    print("\tB) Quit")
    option = input("Enter an option:  ")
    if option.upper() == 'B':
        sys.exit()
    elif option.upper() == 'A':
        display_menu_2()

def display_menu_2():
    result = ""
    print("A)  Panthers")
    print("B)  Bandits")
    print("C)  Warriors")
    user_input = input("Enter an option:  ")
    if user_input.upper() == 'A':
        print(f"Team: Panthers Stats")
        print("---------------------")
        print(f"Total players: {len(panthers_players)}")
        print("Players on Team:")
        for player in panthers_players:
            result += player['name'] + ","
        print(result)
    elif user_input.upper() == 'B':
        print("Team: Bandits Stats")
        print("---------------------")
        print(f"Total players: {len(bandits_players)}")
        print("Players on Team:")
        for player in bandits_players:
            result += player['name'] + ","
        print(result)
    elif user_input.upper() == 'C':
        print("Team: Warriors Stats")
        print("---------------------")
        print(f"Total players: {len(warriors_players)}")
        print("Players on Team:")
        for player in warriors_players:
            result += player['name'] + ","
        print(result)
    else:
        print("Sorry, there is no your choice.")


def print_player():
    for player in Players_copy:
        print(player)

if __name__ == '__main__':
    clean()
    balance_teams()
    display_menu()