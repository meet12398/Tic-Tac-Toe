import os

def clear():
    os.system( 'clear' )

def display_board(board):
    clear()
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
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 select X or O: ').upper()
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random

def choose_first():
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return (board[position] != 'X' and board[position] != 'O')

def full_board_check(board):
    for i in range (1,10):
        if space_check(board, i) == True:
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('\nPlease enter the position (1-9): '))
    return position

def replay():
    choice = input('Do you want to play again? Enter Y or N ')
    return choice.upper() == 'Y'
print('\n\n***********************')
print('Welcome to Tic Tac Toe!')
print('***********************\n\n')

while True:

    game_board = [' ', '1','2','3','4','5','6','7','8','9']
    
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print('\n' + turn +' will go first!')
    
    ready = input('\nReady to play? Y or N: ')
    
    if ready.upper() == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            display_board(game_board)
        
            position = player_choice(game_board)
        
            place_marker(game_board,player1_marker, position)
        
            if win_check(game_board,player1_marker):
                display_board(game_board)
                print('Player 1 has won!!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
                    
        else:
            display_board(game_board)
        
            position = player_choice(game_board)
        
            place_marker(game_board,player2_marker, position)
        
            if win_check(game_board,player2_marker):
                display_board(game_board)
                print('Player 2 has won!!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
                
    if not replay():
        break