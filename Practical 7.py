#shuffle deck
"""
import random

suits=["heart","spade","diamond","club"]
ranks=['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']

deck=[rank+"of"+suit for suit in suits for rank in ranks]

random.shuffle(deck)

print("shuffle deck")
for card in deck:
    print(card)
"""
#Tic tac toc

board = ['_' for i in range(9)]
player = "X"


def show_board():
    print(f'|{board[0]}|{board[1]}|{board[2]}|')
    print(f'|{board[3]}|{board[4]}|{board[5]}|')
    print(f'|{board[6]}|{board[7]}|{board[8]}|')


def is_winner(p):
    return (
        (board[0] == p and board[1] == p and board[2] == p) or
        (board[3] == p and board[4] == p and board[5] == p) or
        (board[6] == p and board[7] == p and board[8] == p) or
        (board[0] == p and board[3] == p and board[6] == p) or
        (board[1] == p and board[4] == p and board[7] == p) or
        (board[2] == p and board[5] == p and board[8] == p) or
        (board[0] == p and board[4] == p and board[8] == p) or
        (board[2] == p and board[4] == p and board[6] == p)
    )


def is_tie():
    return '_' not in board


def game():
    global player

    while True:
        show_board()

        try:
            move = int(input(f"Player {player} enter 0-8: "))

            if 0 <= move <= 8 and board[move] == '_':
                board[move] = player

                if is_winner(player):
                    show_board()
                    print(f"Player {player} wins!")
                    break

                elif is_tie():
                    show_board()
                    print("It's a tie!")
                    break

                if player == "X":
                    player = "O"
                else:
                    player = "X"

            else:
                print("Invalid move! Try again.")

        except ValueError:
            print("Invalid input! Enter number 0-8.")


game()
