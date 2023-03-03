# Author: Robert L Barrera
# Class: CS474, Spring 2019
# Homework 4 : GameController Class
# System: Windows 10
# April 1, 2019

from Board import Board
from Player import Player
from KeyboardConsoleInput import KeyboardConsoleInput


class Connect4Runner:
	def __init__(self):
		self.connect_4 = Board()
		self.player_1 = Player('Player 1', 'R')
		self.player_2 = Player('Player 2', 'B')

	def reinitialize(self):
		self.connect_4 = Board()

	def play_game(self):
		game_being_played = True

		while game_being_played:
			self.connect_4.set_spacing(int(input("Please choose the board spacing: ")))
			print("Type the column in which you wish to move.")
			self.connect_4.print_board()
			no_winner = True
			turn_count = 1
			cur_player = self.player_1

			while no_winner:    # play game
				self.prompt_for_move(turn_count, cur_player.get_player_name(),
				                     cur_player.get_player_type())
				column_input = int(input())
				if not self.col_input_check(column_input):
					continue
				self.connect_4.add_piece(column_input, cur_player.get_player_type())
				self.connect_4.print_board()
				no_winner = not self.check_if_winner(cur_player.get_player_type())
				if not no_winner:
					print("{} Wins!  Play again? (y/n): ".format(cur_player.get_player_name()), end='')
					yes_no = str(input())
					if yes_no == 'n':
						game_being_played = False
					break
				else:
					if self.connect_4.is_board_full():
						print("Tie Game!  Play again? (y/n): ", end='')
						yes_no = str(input())
						if yes_no == 'n':
							game_being_played = False
						break
				turn_count += 1
				if cur_player is self.player_1:
					cur_player = self.player_2
				else:
					cur_player = self.player_1
			self.reinitialize()
		print("Goodbye!")

	def check_if_winner(self, player_type):
		cells = self.connect_4.get_cells()
		if self.check_horizontal(cells, player_type):
			return True
		if self.check_vertical(cells, player_type):
			return True
		if self.check_diagonal(cells, player_type):
			return True
		return False

	def check_horizontal(self, cells, player_type):
		for j in range(6):  # row
			for i in range(0, 4):   # column
				count = 0
				for k in range(0, 4):   # 4 in a row
					if cells[i+k][j].is_occupied():
						if cells[i+k][j].piece.get_player_type() == player_type:
							count += 1
						else:
							break
					else:
						break
				if count == 4:
					return True
		return False

	def check_vertical(self, cells, player_type):
		for i in range(7):  # column
			for j in range(0, 3):  # row
				count = 0
				for k in range(0, 4):  # 4 in a column
					if cells[i][j+k].is_occupied():
						if cells[i][j+k].piece.get_player_type() == player_type:
							count += 1
						else:
							break
					else:
						break
				if count == 4:
					return True
		return False

	def check_diagonal(self, cells, player_type):
		if self.from_up_left(0, 2, 1, cells, player_type) or self.from_up_left(3, 0, 1, cells, player_type):
			return True
		if self.from_up_left(0, 1, 2, cells, player_type) or self.from_up_left(2, 0, 2, cells, player_type):
			return True
		if self.from_up_left(0, 0, 3, cells, player_type) or self.from_up_left(1, 0, 3, cells, player_type):
			return True
		if self.from_bot_left(0, 3, 1, cells, player_type) or self.from_bot_left(3, 5, 1, cells, player_type):
			return True
		if self.from_bot_left(0, 4, 2, cells, player_type) or self.from_bot_left(2, 5, 2, cells, player_type):
			return True
		if self.from_bot_left(0, 5, 3, cells, player_type) or self.from_bot_left(1, 5, 3, cells, player_type):
			return True
		return False

	def from_up_left(self, col_start, row_start, dis, cells, player_type):
		for i in range(dis):  # number of times to check
			count = 0
			for j in range(0, 4):  # 4 to count
				if cells[col_start+i+j][row_start+i+j].is_occupied():
					if cells[col_start+i+j][row_start+i+j].piece.get_player_type() == player_type:
						count += 1
					else:
						break
				else:
					break
			if count == 4:
				return True
		return False

	def from_bot_left(self, col_start, row_start, dis, cells, player_type):
		for i in range(dis):  # number of times to check
			count = 0
			for j in range(0, 4):  # 4 to count
				if cells[col_start + i + j][row_start - i - j].is_occupied():
					if cells[col_start + i + j][row_start - i - j].piece.get_player_type() == player_type:
						count += 1
					else:
						break
				else:
					break
			if count == 4:
				return True
		return False

	def prompt_for_move(self, turn_count, player_name, player_symbol):
		print("Turn {}: {} ({}), choose your move: ".format(turn_count, player_name, player_symbol), end='')

	def invalid_move_out_of_bounds(self):
		print("Invalid move, outside board, try again: ")

	def col_full_error(self, loc):
		print("Invalid move, column {} is full, try again: ".format(loc))

	def col_input_check(self, col):
		if not self.connect_4.is_move_in_bounds(col):
			self.invalid_move_out_of_bounds()
			return False
		if not self.connect_4.is_move_allowed(col):
			self.col_full_error(col)
			return False
		return True
