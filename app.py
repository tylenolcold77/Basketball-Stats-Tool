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
    pass


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
            print(f"{player['name']}")
    elif user_input.upper() == 'B':
        print("Team: Bandits Stats")
        print("---------------------")
        print(f"Total players: {len(bandits_players)}")
        print("Players on Team:")
        print(f"{player['name']}")
    elif user_input.upper() == 'C':
        print("Team: Warriors Stats")
        print("---------------------")
        print(f"Total players: {len(warriors_players)}")
        print("Players on Team:")
        print(f"{player['name']}")
    else:
        print("Sorry, there is no your choice.")


def print_player():
    for player in Players_copy:
        print(player)

if __name__ == '__main__':
    clean()
    balance_teams()
    display_menu()