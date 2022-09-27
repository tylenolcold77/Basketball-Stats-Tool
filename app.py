import constants
import random
import sys

#Players_copy = constants.PLAYERS
#Team_copy = constants.TEAMS
num_players_team = int(len(constants.PLAYERS) / len(constants.TEAMS))
cleaned_player_list = []
cleaned_player_set = set()
panthers_players = []
bandits_players = []
potential_bandits_players = []
warriors_players = []





#print(len(Players_copy))
def clean():
    for player in constants.PLAYERS:
        fixed = {}
        fixed['name'] = player['name']
        fixed['guardians'] = player['guardians']
        fixed['experience'] = player['experience']

        fixed['height'] = int(player['height'].split(" ")[0])
        #print(fixed['height'])
        if player['experience'] == 'YES':
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        cleaned_player_list.append(fixed)

    
        #print(fixed['experience'])
    return cleaned_player_list


def balance_teams():
    available_ids = range(len(constants.PLAYERS))
    # pick first team
    panthers_ids = random.sample(available_ids, num_players_team)
    # remove choices from available list
    available_ids = [id for id in available_ids if id not in panthers_ids]
    # repeat for next team
    bandits_ids = random.sample(available_ids, num_players_team)
    available_ids = [id for id in available_ids if id not in bandits_ids]
    # anyone not picked goes in last team
    warriors_ids = available_ids
    # finally, populate the object lists
    global panthers_players, warriors_players, bandits_players
    panthers_players = [constants.PLAYERS[id] for id in panthers_ids]
    bandits_players  = [constants.PLAYERS[id] for id in bandits_ids]
    warriors_players = [constants.PLAYERS[id] for id in warriors_ids]


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
    else:
        print("InPut Error.")

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
        for player in bandits_players:
            print(f"{player['name']}")
    elif user_input.upper() == 'C':
        print("Team: Warriors Stats")
        print("---------------------")
        print(f"Total players: {len(warriors_players)}")
        print("Players on Team:")
        for player in warriors_players:
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