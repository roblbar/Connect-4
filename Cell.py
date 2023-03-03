# Author: Robert L Barrera
# Class: CS474, Spring 2019
# Homework 4 : Cell Class
# System: Windows 10
# April 1, 2019

from Piece import Piece


class Cell:
	"""Cell location on a game board."""
	def __init__(self, col, row):
		"""Set column, row, piece, and occupation status."""
		self.col = col
		self.row = row
		self.piece = None
		self.occupied = False

	def get_col(self):
		"""Return cell's column."""
		return self.col

	def get_row(self):
		"""Return cell's row."""
		return self.row

	def is_occupied(self):
		"""Return cell's occupation status."""
		return self.occupied

	def set_piece(self, player_type):
		"""Set a piece into cell and set occupation to true."""
		self.piece = Piece(player_type, self.col, self.row)
		self.occupied = True
