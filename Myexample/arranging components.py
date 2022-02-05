############# Display The List ###################

game_list = ['0','1','2']
def display_game(game_list):
    print(f"Here is the current list: {game_list}")

############# Take Input and if not provided correct input....show message accordingly ################

def position_choice():
    choice = "Wrong"

    while choice not in ['0','1','2']:
        choice = input("Pick a position (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry, Invalid choice ")

    return int(choice)


############## Code for Replacement ##############

def replacement(game_list,position):
    replace = input(f"Type a string to place at position: ")
    game_list[position] = replace
    return game_list


############# The Game must continue ############

def continue_play():
    choice = "Wrong"

    while choice not in ['Y','N']:
        choice = input("You want to keep playing (Y or N): ")
        if choice not in ['Y','N']:
            print("Sorry, I don't understand, please choose Y or N!!")

    if choice == "Y":
        return True
    else:
        return False

############### Combine Everything ###############

game_on = True
game_list = ['0','1','2']

while game_on:

    display_game(game_list)
    position = position_choice()
    game_list = replacement(game_list,position)
    display_game(game_list)
    game_on = continue_play()