"""
@author: kamal
"""
from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
    
def player_input():
    marker = 'WRONG'
    
    while marker not in ['X', 'O']:
        marker = input("Would you like to be X or O? ")
        
        if marker not in ['X', 'O']:
            print("I did not recognise that, please try again")

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
import random

def choose_first():
    num = random.randint(0,1)
    if num == 1:
        return 'Player 1'
    else:
        return 'Player 2'
    
    
def player_choice(board):
    choice = 'WRONG'
    
    while choice not in range(1,10):
        choice = int(input('Choose your next position: (1-9): '))
            
        if choice in range (1,10):
            if space_check(board, choice):
                return choice

def place_marker(board, marker, position):
    board[position] = marker
    

def space_check(board, position):
    if board[position] not in ['X','O']:
        return True
    else:
        return False

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal    