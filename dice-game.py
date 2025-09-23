####
# The tranlated exercise (by deepl.com):
#
# We want a programme to play a simple, two-player game, moving forward one square per turn. 
# The players will roll real dice and tell the programme the results.
# The programme will control the turns, telling each player where they are and checking the special squares, which are multiples of 5. 
# 
# If a player lands on a square that is a multiple of 10, they roll again.
# If they land on a multiple of 5, but not 10, they will lose their next turn.
# 
# The programme will ask how many squares the game has (i.e. the number of the goal) and will end when a player reaches it exactly. 
# If they go over, they will bounce back as many squares as they have exceeded.
# 
# Note
# It is mandatory to use at least one other function, in addition to main, with a size divided into similar parts and passing of
# arguments.
####

class Player:
    """Player class, stores the name, position and has_skipped-state of a player.

    Attributes
    ----------
    position : int
        the current position of the player on the board
    name : str
        the name of the player for easier readability
    has_skipped : boolean
        a helper-boolean to ensure a player is only skipped once

    Methods
    -------
    __init__(name=None)
        sets the inital name of the player
    
    """  
    
    position = 1
    name = None
    has_skipped = False

    def __init__(self, name: str):
        self.name = name
        

def get_num_input() -> int:
    """Function to get an integer from the cli-input.

    Attention: Provided Values will be cast to an Integer, so floats will be lost.
    Should the provided value not be castable to an Integer, the prompt will be tried again for three times, bevore exiting the process.
    """

    for i in range(3):
        number = input("number: #")
        try:
            return int(number)
        except ValueError:
            print("The number is not valid, please try again")
    exit(1) # The programm ends cleanly with an error-code


def new_player_position(player_position: int, dice_roll: int, total_number_of_squares: int) -> int:
    """Function to calculate the new player position on the board.

    Handles the case, that a player can't exit the board at the end, but bounces back the number of fields, he would have gone too far.
    """

    new_player_position = player_position + dice_roll
    # if we get out of bounds, bounce back, by the number of fields, we went to far
    if new_player_position > total_number_of_squares:
        new_player_position = total_number_of_squares - (new_player_position - total_number_of_squares)
    return new_player_position


def game_round(current_player: Player, total_number_of_squares: int) -> Player|None:
    """Function that represents one round for one player to be played.

    This function handles everything from checking, 
    if a player needs to be skipped or can roll again, 
    as well as checking the win condition.
    """

    winner = None

    print("It's the turn of player %s, that is currently on position: %s" % (current_player.name, current_player.position))

    # check if player has to skip his round
    if ((current_player.position % 5) == 0 and (current_player.position % 10) != 0) and current_player.has_skipped == False:
        print("The player: %s has to skip his round" % current_player.name)
        current_player.has_skipped = True
        return winner
    current_player.has_skipped = False # reset the has_skipped value

    # normal round handling
    print("Please roll the dice for the current player: %s and enter the sum." % current_player.name)
    dice_roll = get_num_input()
    current_player.position = new_player_position(current_player.position, dice_roll, total_number_of_squares)

    # check if player is on a 10*x field, then let him roll again (this can continue indefinetly)
    if (current_player.position % 10) == 0:
        print("The player: %s can go again!" % current_player.name)
        return game_round(current_player, total_number_of_squares)

    # check if the player has won
    if current_player.position == total_number_of_squares:
        winner = current_player
    # return if the player won
    return winner


def game(total_number_of_squares: int, player_1: Player, player_2: Player):
    """This function represents the default gameloop.

    It repeats alternating turns until one player wins.
    """


    # define the game loop: the game goes on, until somebody wins
    winner = None
    while winner == None :
        winner = game_round(player_1, total_number_of_squares)
        if winner != None:
            continue # skip the second player, if player_1 has already won
        winner = game_round(player_2, total_number_of_squares)
    
    print("Congratulation!!!! Player %s won the game!" % winner.name)


def main():
    """The default entrypoint for the game."""
    total_number_of_squares = 0      # The total number of squares

    # initiate game
    print("Please enter the number of squares you want to play with. Only integer values are valid.")
    total_number_of_squares = get_num_input()
    player_1 = Player("Player_1")
    player_2 = Player("Player_2")

    game(total_number_of_squares, player_1, player_2)


if __name__ == "__main__":
    main()
