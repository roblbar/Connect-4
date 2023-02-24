# Author: Robert L Barrera
# NetID: rbarre4    ACCC: rbarrera
# Class: CS474, Spring 2019
# Homework 4 : Piece Class
# System: Windows 10
# April 1, 2019


class Piece:
	"""Piece to go on a board."""
	def __init__(self, player, col, row):
		"""Set player, column, and row."""
		self.player = player
		self.col = col
		self.row = row

	def get_player_type(self):
		"""Return piece's player type."""
		return self.player

	def get_col(self):
		"""Return piece's column."""
		return self.col

	def get_row(self):
		"""Return piece's row."""
		return self.row
