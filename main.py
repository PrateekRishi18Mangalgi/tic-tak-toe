import os
import random

def clear_screen():
    # Clear the console screen for Windows or Linux/MacOS
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board):
    clear_screen()

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input('Player 1: Do you want to be X or O? ').upper()
    return ('X', 'O') if marker == 'X' else ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (
        (board[7] == board[8] == board[9] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[1] == board[2] == board[3] == mark) or
        (board[7] == board[4] == board[1] == mark) or
        (board[8] == board[5] == board[2] == mark) or
        (board[9] == board[6] == board[3] == mark) or
        (board[7] == board[5] == board[3] == mark) or
        (board[9] == board[5] == board[1] == mark)
    )

def choose_first():
    return 'Player 1' if random.randint(0, 1) == 0 else 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return not any(space_check(board, i) for i in range(1, 10))

def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input('Choose your next position (1-9): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 9.')
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    game_on = input('Are you ready to play? Enter Yes or No: ').lower().startswith('y')

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            elif full_board_check(theBoard):
                display_board(theBoard)
                print('The game is a draw!')
                break
            else:
                turn = 'Player 2'

        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            elif full_board_check(theBoard):
                display_board(theBoard)
                print('The game is a draw!')
                break
            else:
                turn = 'Player 1'

    if not replay():
        break
