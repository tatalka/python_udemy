import os
def draw_board(board_schema):
	print('-------------')
	print('| {} | {} | {} |'.format(board_schema[2][0], board_schema[2][1], board_schema[2][2]))
	print('-------------')
	print('| {} | {} | {} |'.format(board_schema[1][0], board_schema[1][1], board_schema[1][2]))
	print('-------------')
	print('| {} | {} | {} |'.format(board_schema[0][0], board_schema[0][1], board_schema[0][2]))
	print('-------------')

def clear_screen():
	os.system('cls')	

def introduction():
	print('Players use numpad for placing X or O')
	print(' ')

def place_a_marker():
	text = input('please enter some text')
	print(text)

def take_user_input(mark, board_schema):
	mark_position = input('Input field on numpad and press Enter: ')
	if(mark_position == '1'):
		board_schema[0][0] = mark
	elif(mark_position == '2'):
		board_schema[0][1] = mark
	elif(mark_position == '3'):
		board_schema[0][2] = mark
	elif(mark_position == '4'):
		board_schema[1][0] = mark
	elif(mark_position == '5'):
		board_schema[1][1] = mark
	elif(mark_position == '6'):
		board_schema[1][2] = mark
	elif(mark_position == '7'):
		board_schema[2][0] = mark
	elif(mark_position == '8'):
		board_schema[2][1] = mark
	elif(mark_position == '9'):
		board_schema[2][2] = mark
	elif(mark_position == '0'):
		exit()
	else:
		pass

def switch_player(player):
	if(player == 'X'):
		player = 'Y'
	else:
		player = 'X'
	return player

def check_if_win(board_schema):
	pass

def check_if_board_full(board_schema):
	my_list = []
	for element in board_schema:
		for sub in element:
			my_list.append(sub)
	
	is_table_full = True
	for element in my_list:
		if element == ' ':
			is_table_full = False

	if(is_table_full == True):
			print("Table is full, end game, it's a tie")
			exit()

def check_if_won(board_schema, player):
	# first check if winning column
	if(board_schema[0][0] == board_schema[0][1] == board_schema[0][2] and board_schema[0][0] != ' '):
		print('Player %s won!' %player)
		exit()
	if(board_schema[1][0] == board_schema[1][1] == board_schema[1][2] and board_schema[1][0] != ' '):
		print('Player %s won!' %player)
		exit()
	if(board_schema[2][0] == board_schema[2][1] == board_schema[2][2] and board_schema[2][0] != ' '):
		print('Player %s won!' %player)
		exit()
	# then check if winning row
	if(board_schema[0][0] == board_schema[1][0] == board_schema[2][0] and board_schema[0][0] != ' '):
		print('Player %s won!' %player)
		exit()
	if(board_schema[0][1] == board_schema[1][1] == board_schema[2][1] and board_schema[0][1] != ' '):
		print('Player %s won!' %player)
		exit()
	if(board_schema[0][2] == board_schema[1][2] == board_schema[2][2] and board_schema[0][2] != ' '):
		print('Player %s won!' %player)
		exit()
	# last check if winning diagonal
	if(board_schema[0][0] == board_schema[1][1] == board_schema[2][2] and board_schema[0][0] != ' '):
		print('Player %s won!' %player)
		exit()
	if(board_schema[0][2] == board_schema[1][1] == board_schema[2][0] and board_schema[0][2] != ' '):
		print('Player %s won!' %player)
		exit()		


def tic_tac_toe(player):
	clear_screen()
	introduction()
	draw_board(board_schema)

	while (True):
		take_user_input(player, board_schema)
		clear_screen()
		print('Current table :')
		draw_board(board_schema)
		check_if_board_full(board_schema)
		check_if_won(board_schema, player)
		player = switch_player(player)
		
		

board_schema = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

tic_tac_toe('X')


