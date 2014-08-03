# stdlib imports
from sys import maxsize
import pdb
import os
import logging

# core django imports
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

# 3rd party imports

# project imports
#from .formsrevision import PdbForm
#from .models import Pdb
#from settings.base import get_env_variable

# log all errors for debugging
logger = logging.getLogger('infolog')


best_value = 20
win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
board = ['' for index in range(9)]
best_move = 0

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

def get_available_positions(board):
	#available_positions = []
	available_positions = [ind for ind,val in enumerate(board) if val == '']
	return available_positions

def minimax(board, player, depth, best_value):
	print("###### START MINIMAX ===== depth = %s"%depth)
	best_val_list = []
	best_position_list = []
	best_value = best_value if player == 'x' else -best_value
	if has_won(board,player):
		return (10 - depth) if player == 'x' else (depth - 10)

	elif has_tied(board):
		return 0

	else:
		copy_of_board = board[:]
		available_positions = get_available_positions(copy_of_board)
		print ("available_positions= %s"%available_positions)

		for position in available_positions:
			depth += 1
			#print("========= start for-loop on position = %s at depth = %s ========="%(position, depth))
			player = 'o' if player == 'x' else 'x'
			copy_of_board[position] = player
			game_state_value = minimax(copy_of_board, player, depth, best_value)
			if abs(game_state_value) < abs(best_value):
				best_value = game_state_value
			else:
				best_value = best_value
			best_val_list.append(best_value)
			best_position_list.append(position)
			#print("========== end for-loop on position = %s at depth = %s ========="%(position, depth))

		if player == 'x':
			value,index = max( (v, i) for i, v in enumerate(best_val_list) )
		else:
			value, index = min( (v, i) for i, v in enumerate(best_val_list) )

		print("best_val_list = %s"%best_val_list)
		print("best_position_list = %s"%best_position_list)
		print("******* best_val_list[%s] = %s, best_position_list[%s] = %s *******\n"%(index,value, index,best_position_list[index]))
		best_move = best_position_list[index]
		print("###### END MINIMAX === depth = %s, value = %s, index = %s"%(depth, value, index))
		return value #, best_position_list[index]

def tictactoeviews(request):
	if request.method == "POST" and request.is_ajax():
		pass
	else:
		render_to_response('index.html', context={}, context_instance=RequestContext(request))
