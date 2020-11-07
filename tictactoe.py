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