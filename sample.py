import os

def clear_screen():
	os.system('cls')

def display_board(board):
	print('  |   |')
	print('---------')
	print('  |   |')
	print('---------')
	print('  |   |')

display_board([])
