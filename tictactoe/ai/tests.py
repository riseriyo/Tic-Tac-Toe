from django.test import TestCase
from django.utils import unittest
#import unittest

#from .models import Entry, Comment
#from .forms import CommentForm
from .views import has_won
from .views import has_tied
from .views import has_empty_squares

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
