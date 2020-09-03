#------- GLOBAL VARRIABLES -------

game_still_going = True

winner = None

# X is default start player
current_player = "X"

# Innitial Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2]+"    1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5]+"    4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8]+"    7 | 8 | 9")
    print("\n")
    
def play_game():
    
    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner =="X" or winner =="O":
        pint(winner + " won.")
    elif winner == None:
        print("Tie Game.")

def handle_turn(player):

    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    board[position] = "X"

    display_board()


def check_if_game_over():
    check_for_winner()

    check_if_tie()

def check_for_winner():
    check_diag()
    check_col()
    check_row()

def check_diag():

def check_col():

def check_row():

def check_if_tie():


def flip_player():

