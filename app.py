# imports constants from constants.py
import constants

def clean_data():
    """
    clean_data will iterate through the constant PLAYER and adjust the following information:
    - EXPERIENCE will be changed to a bool value (no = false; yes = true)
    - HEIGHT will parse the string for the players height (int)
    - GUARDIANS will change the string into a list of gardians ()
    """

    temp_players = []
    temp_player = {}

    for player in constants.PLAYERS:
        
        keys = list(player.keys())

        for key in keys:
            if key.upper() == "EXPERIENCE":
                if player[key].upper() == "NO":
                    temp_player[key] = False
                else:
                    temp_player[key] = True
            elif key.upper() == "HEIGHT":
                temp_player[key] = int(player[key].split()[0])
            elif key.upper() == "GUARDIANS":
                temp_player[key] = player[key].split(" and ")
            else:
                temp_player[key] = player[key]

        temp_players.append(temp_player)
        temp_player = {}

    return temp_players


def balance_teams(players):
    """
    docstring
    """
    teams = []

    experienced_players = []
    non_experienced_players = []

    for player in players:
        if player["experience"] == True:
            experienced_players.append(player)
        else:
            non_experienced_players.append(player)

    for team in constants.TEAMS:
        teams.append({"name":team, "players":[], "experienced":0, "inexperienced":0 })

    for index, player in enumerate(experienced_players):
        teams[index%len(teams)]["players"].append(player)
        teams[index%len(teams)]["experienced"] += 1

    for index, player in enumerate(non_experienced_players):
        teams[index%len(teams)]["players"].append(player)
        teams[index%len(teams)]["inexperienced"] += 1

    return teams

def get_user_input():
    return input("\nEnter an option > ")

def display_menu():
    print("\nBASKETBALL TEAM STATS TOOL\n")
    print("---- MENU ----\n")
    print("Here are your choices:\n")
    print("     1.) Display team stats")
    print("     2.) Quit")

def display_teams(teams):
    """
    docstring
    """
    print("\n")
    for index, team in enumerate(teams,1):
        print("{}.) {}".format(index, team["name"]))

    team_selected = False

    while not team_selected:
        try:
            user_input = int(get_user_input())
        except ValueError as err:
            print("We experienced an error with your selection ({}). Please try again.".format(err))
        else:
            if (user_input >= 1 and user_input <= len(teams)):
                display_team(teams[user_input-1])
                team_selected = True
            else:
                print("You did not select a valid option. Please try again.")
            
    

def display_team(team):
    """
    docstring
    """

    total_height = 0.0
    player_list = []
    guardian_list = []

    for player in team["players"]:
        total_height += player["height"]
        player_list.append(player["name"])
        for guardian in player["guardians"]:
            guardian_list.append(guardian)

    average_height = total_height / len(team["players"])

    print("\nTeam: {} stats".format(team["name"]))
    print("-"*20)
    print("Total players: {}".format(len(team["players"])))
    print("Total experienced: {}".format(team["experienced"]))
    print("Total inexperienced: {}".format(team["inexperienced"]))
    print("Average Height: {}".format(round(average_height, 2)))
    print("\nPlayers on team:")
    print(", ".join(player_list))
    print("\nGuardians:")
    print(", ".join(guardian_list))
    input("\nPress ENTER to continue...")



if __name__ == "__main__":

    players = clean_data()
    teams = balance_teams(players)

    quit = False

    while not quit:

        display_menu()
        
        try:
            user_input = int(get_user_input())
        except ValueError:
            print("We experienced an error with your input. Please try entering a number.")
        else:
            if user_input == 1:
                display_teams(teams)
            elif user_input == 2:
                quit = True
            else:
                print("You did not select a valid option. Please try again.")
            

