from django.test import TestCase
from django.utils import unittest
from django.core.urlresolvers import reverse
from django.test.client import Client
#import unittest

#from .models import Entry, Comment
#from .forms import CommentForm
from .views import has_won
from .views import has_tied
from .views import has_empty_squares
from .views import get_available_positions
from .views import minimax

class MiniMaxTest(unittest.TestCase):
	'''Tests for minimax function'''

	def setUp(self):
		win_combos = [	[0, 1, 2], [3, 4, 5], [6, 7, 8],
						[0, 3, 6], [1, 4, 7], [2, 5, 8],
						[0, 4, 8], [2, 4, 6]
					]

	def test_x_has_won(self):
		board = ['x', 'o', '', 'x', '', '', 'x', 'x', 'o']
		player = 'x'
		result = has_won(board, player)
		self.assertEqual(result, True)

	def test_x_has_not_won(self):
		board = ['x', 'o', '', '', '', '', 'x', 'x', 'o']
		player = 'x'
		result = has_won(board,player)
		self.assertEqual(result,False)

	def test_has_empty_squares(self):
		board =  ['', '', '', '', '', '', '', '', '']
		result = has_empty_squares(board)
		self.assertEqual(result, True)

	def test_has_one_empty_square(self):
		board = ['x', 'o', 'x', 'x', 'o', 'o', 'o', 'x', '']
		result = has_empty_squares(board)
		self.assertEqual(result, True)

	def test_has_tied(self):
		board = ['x', 'o', 'x', 'o', 'x', 'x', 'o', 'x', 'o']
		result = has_tied(board)
		self.assertEqual(result, True)

	def test_has_not_tied(self):
		board = ['x', 'o', 'x', 'x', 'o', 'x', 'o', '', '']
		result = has_tied(board)
		self.assertEqual(result, False)

	def test_get_available_moves(self):
		board = ['', 'x', '', '', '', 'x', 'o', 'o', 'x']
		result = get_available_positions(board)
		self.assertEqual(len(result), 4)

	def test_x_2nd_example_best_block_move_square(self):
		board = ['', 'x', '', '', '', 'x', 'o', 'o', 'x']
		best_value = 20
		depth = 0
		player = 'x' # 6 x-wins o's best move to block x
		result = minimax(board, player, depth, best_value)
		self.assertEqual(result, 8) #8, 2
		#self.assertEqual(result, (8, 2))

	def test_o_2nd_example_best_block_move_square(self):
		board = ['', 'x', '', '', '', 'x', 'o', 'o', 'x']
		best_value = 20
		depth = 0
		player = 'o' # -6 x's best move to block o
		result = minimax(board, player, depth, best_value)
		self.assertEqual(result, -6) #-6, 0
		#self.assertEqual(result, (-6, 0))

	def test_o_turn_best_block_move_square(self):
		board = ['x', 'o', 'x', 'o', 'x', 'o', '', '', '']
		best_value = 20
		depth = 0
		player = 'o' # 9 x-wins x's best move to block o
		result = minimax(board, player, depth, best_value)
		self.assertEqual(result, 9) #9, 6
		#self.assertEqual(result, (9, 6))

	def test_x_turn_best_block_move_square(self):
		board = ['x', 'o', 'x', 'o', 'x', 'o', '', '', '']
		best_value = 20
		depth = 0
		player = 'x' # 0 tie o's best move to block x
		result = minimax(board, player, depth, best_value)
		self.assertEqual(result, 0) #0,6
		#self.assertEqual(result, (0,6))

	def test_x_ties_minimax(self):
		board = ['x', 'o', 'x', 'x', 'o', 'x', 'o', '', '']
		best_value = 20
		depth = 0
		player = 'x' # 0 best_value x's best move to block o
		result = minimax(board, player, depth, best_value)
		self.assertEqual(result, 8) #8,8
		#self.assertEqual(result, (8,8))

	def test_o_ties_minimax(self):
		board = ['x', 'o', 'x', 'x', 'o', 'x', 'o', '', '']
		best_value = 20
		depth = 0
		player = 'o' # 0 best_value x's best move to block o
		result = minimax(board, player, depth, best_value)
		self.assertEqual(result, 0) #0,7
		#self.assertEqual(result, (0,7))


class TicTacToeViewsTest(TestCase):

	def test_tttviews(self):
		c = Client()
		response = c.get(reverse('tictactoe'))
		print response
		self.assertEqual(response.status_code, 200)

	def test_post_tttviews(self):
		c = Client()
		# from frontend pass back an array in a json object?
		response = c.post('tictactoe', {'0':['x', 'o', 'x', 'x', 'o', 'x', 'o', '', '']})
		self.assertEqual(response)
