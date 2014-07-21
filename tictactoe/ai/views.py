from django.shortcuts import render

win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
board = ['' for index in range(9)]

def minimax(board, player):
	if hasWon(board,player):
		if player == 'x':
			return 'X wins!'
		else:
			return "O wins!"
	elif has_tied(board):
		return "It's a tie!"

	else:
		pass

def has_won(board, player):
	combo_list = []
	frequency_dict = {}
	board_positions = [ind for ind, val in enumerate(board) if val == player]
	combo_list = [combo for position in board_positions for combo in win_combos if position in combo]
	frequency_dict = {str(x): combo_list.count(x) for x in combo_list}
	for key,val in frequency_dict.items():
		if val == 3:
		    return True
	return False

def has_tied(board):
	if has_empty_squares(board):
		return False
	return True

def has_empty_squares(board):
	board_positions = [ind for ind,val in enumerate(board) if val == 'x' or val == 'o']
	if len(board_positions) < 9:
		return True
	return False
