# Author: Robert L Barrera
# NetID: rbarre4    ACCC: rbarrera
# Class: CS474, Spring 2019
# Homework 4 : Player Class
# System: Windows 10
# April 1, 2019


class Player:
	"""Player for a game."""
	def __init__(self, name, color_type):
		"""Set name and color type."""
		self.name = name
		self.color_type = color_type

	def get_player_type(self):
		"""Return player's type."""
		return self.color_type

	def get_player_name(self):
		"""Return player's name."""
		return self.name

	def choose_move(self):
		"""Not implemented."""
		pass
