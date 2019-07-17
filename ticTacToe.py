# based on https://inventwithpython.com/chapter10.html for practice

# tic tac toe game

import random
import time


def get_letter():
    while True:
        letter = input("Choose your letter ('X' or 'O') >> ")
        if letter.upper() == 'X':
            return['X', 'O']
        elif letter.upper() == 'O':
            return['O', 'X']
        else:
            print("You must enter 'X' or 'O'")


def flip_coin():
    print("Flipping coin to choose first player...")
    time.sleep(3)
    outcome = random.randint(0, 1)

    if outcome == 0:
        return "player"
    else:
        return "computer"


def generate_board(board):
    print("")
    print(" --- --- --- ")
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |")
    print(" --- --- --- ")
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print(" --- --- --- ")
    print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print(" --- --- --- ")
    print("")


def get_move(board):
    while True:
        move = int(input("Enter your move (1 - 9) >> "))
        if space_free(board, move):
            return move
        else:
            print("You cannot play this square")


def make_move(board, move, letter):
    board[move] = letter


def winning_position(board, letter):
    if (board[1] == letter and board[2] == letter and board[3] == letter)\
        or (board[4] == letter and board[5] == letter and board[6] == letter)\
        or (board[7] == letter and board[8] == letter and board[9] == letter)\
        or (board[1] == letter and board[4] == letter and board[7] == letter)\
        or (board[2] == letter and board[5] == letter and board[8] == letter)\
        or (board[3] == letter and board[6] == letter and board[9] == letter)\
        or (board[1] == letter and board[5] == letter and board[9] == letter)\
        or (board[3] == letter and board[5] == letter and board[7] == letter):
        return True
    else:
        return False


def get_duplicate_board(board):
    duplicate_board = []

    for i in board:
        duplicate_board.append(i)

    return duplicate_board


def space_free(board, move):
    if board[move] is not " ":
        return False
    else:
        return True


def random_move(board, spaces):
    moves = []
    for i in spaces:
        if space_free(board, i):
            moves.append(i)

    if len(moves) is not 0:
        return random.choice(moves)
    else:
        return None


def get_computer_move(board, computer_letter, player_letter):

    for i in range(1, 10):
        board_copy = get_duplicate_board(board)
        if space_free(board_copy, i):
            make_move(board_copy, i, computer_letter)
            if winning_position(board_copy, computer_letter):
                return i

    for i in range(1, 10):
        board_copy = get_duplicate_board(board)
        if space_free(board_copy, i):
            make_move(board_copy, i, player_letter)
            if winning_position(board_copy, player_letter):
                return i

    move = random_move(board, [1, 3, 7, 9])
    if move is not None:
        return move

    if space_free(board, 5):
        return 5

    return random_move(board, [2, 4, 6, 8])


def board_full(board):
    for i in range(1, 10):
        if space_free(board, i):
            return False
    return True


def play_again():
    answer = input("Would you like to play again? >> ")
    return answer.lower() == "yes"


print("Welcome to tic tac toe!")

while True:
    board = [' '] * 10

    player_letter, computer_letter = get_letter()

    turn = flip_coin()
    print("The " + turn + " will start")

    game_in_progress = True

    while game_in_progress:
        if turn == "player":
            generate_board(board)
            player_move = get_move(board)
            make_move(board, player_move, player_letter)
            if winning_position(board, player_letter):
                print("You have won the game")
                generate_board(board)
                game_in_progress = False
            elif board_full(board):
                generate_board(board)
                print("Tie")
                break
            else:
                turn = "computer"

        elif turn == "computer":
            computer_move = get_computer_move(board, computer_letter, player_letter)
            make_move(board, computer_move, computer_letter)

            if winning_position(board, computer_letter):
                generate_board(board)
                print("You have lost")
                game_in_progress = False
            elif board_full(board):
                generate_board(board)
                print("The game is a tie")
                break
            else:
                turn = 'player'

    if not play_again():
        break

