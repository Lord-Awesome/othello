# Program starts here. You can choose between playing a single game, and training the computer against itself over n iterations

import numpy as np
import os
path = "C:\\Users\\myran\\Desktop" #change for pi
os.chdir(path)

from play_a_game import play_a_game
from board_setup import board_setup
from reset_weight_grid import reset_weight_grid
#reset_weight_grid()  # resets the weight_grid

train = 'no' #Option to train the computer. If no, it plays a single game. If yes, it plays 'iterations' games. print_bool determines if it the program displays output. Recommend 0 for training


if train == 'no':
    board = board_setup()
    print_bool = 1
    black_input = 'starter_input'
    white_input = 'starter_input'
    if print_bool == 1:
        print('Starting board state: ')
        print(board)
    winner = play_a_game(board, print_bool, black_input, white_input)
    x = input('Press Enter to Exit')

if train == 'yes':
    iterations = 1000
    print_bool = 0
    black_input = 'computer_weight_capture'
    white_input = 'computer_random'
    
    winner_list = []
    black_wins = 0
    white_wins = 0
    tie_wins = 0
    
    for game in range(iterations):
        print('-'*100)
        print('                Game ', game+1)
        print('-'*100)

        board= board_setup()
        winner = play_a_game(board, print_bool, black_input, white_input)

        winner_list.append(winner)

        if winner == 'black':
            black_wins += 1
        if winner == 'white':
            white_wins += 1
        if winner == 'tie':
            tie_wins += 1

    print('-' * 100)
    print('-' * 100)
    print('-' * 100)
    print('-' * 100)
          
    print('Weight Grid Summary')
    final_weight_grid = np.load('weight_grid.npy')
    if np.min(np.abs(final_weight_grid)) != 0:
        normalized_grid = np.true_divide(final_weight_grid, np.min(np.abs(final_weight_grid)))
    else:
        normalized_grid = final_weight_grid
    print(normalized_grid)
        
    print('Winning Summary')
    print('Black wins: ', black_wins)
    print('White wins: ', white_wins)
    print('Tie: ', tie_wins)
    print('-'*100)



