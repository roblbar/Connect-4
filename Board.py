# Author: Robert L Barrera
# Class: CS474, Spring 2019
# Homework 4 : Board Class
# System: Windows 10
# April 1, 2019

from Cell import Cell
from Piece import Piece


class Board:
	def __init__(self, col=7, row=6, spacing=None):
		self.col = col
		self.row = row
		if spacing is None or spacing < 0:
			self.spacing = 0
		else:
			self.spacing = spacing-1
		self.cells = []
		for cell_col in range(self.col):
			new_row = []
			for cell_row in range(self.row):
				#print(str(cell_col) + " " + str(cell_row))
				new_row.append(Cell(cell_col, cell_row))
				#print(new_row[cell_row].get_col())
			self.cells.append(new_row)

	def is_move_allowed(self, col):
		if self.cells[col-1][0].is_occupied():
			return False
		else:
			return True

	def is_move_in_bounds(self, col):
		if 0 < col <= self.col:
			return True
		else:
			return False

	def add_piece(self, col, player_type):
		for cell_row in range(self.row):
			if self.cells[col-1][cell_row].is_occupied():
				self.cells[col-1][cell_row-1].set_piece(player_type)
				return
		self.cells[col-1][self.row-1].set_piece(player_type)

	def is_board_full(self):
		for cell_col in range(self.col):
			if not self.cells[cell_col][0].is_occupied():   # Check first row
				return False
		return True

	def set_spacing(self, spacing):
		if spacing is None or spacing < 0:
			self.spacing = 0
		else:
			self.spacing = spacing - 1

	def get_cells(self):
		return self.cells

	'''For printing/testing'''

	def fill_board(self, player_type):
		for cell_row in range(self.row):
			for cell_col in range(self.col):
				a_cell = self.cells[cell_col][cell_row]
				a_cell.set_piece(player_type)

	'''Uses code from Professor Deitz's ASCIIDisplay class'''

	def print_board(self):
		print()
		full_string = ""
		across = range(0, self.col)
		# up = range(0, b.rows, 1)
		#up = range(self.row - 1, -1, -1)
		up = range(0, self.row)
		spaces = range(self.spacing)
		for i in up:
			top = "+"
			for j in across:
				for k in spaces:
					top = top + "-"
				top = top + "-"
				for k in spaces:
					top = top + "-"
				top = top + "+"
			top = top + "\n"
			full_string = full_string + top
			top = "+"
			for j in across:
				for k in spaces:
					top = top + " "
				a_cell = self.cells[j][i]
				if a_cell.is_occupied():
					top = top + a_cell.piece.get_player_type()
				else:
					top = top + ' '
				for k in spaces:
					top = top + " "
				if j == self.col:
					top = top + "+"
				else:
					top = top + "|"
			top = top + "\n"
			full_string = full_string + top
		top = "+"
		# bottom
		for j in across:
			for k in spaces:
				top = top + "-"
			top = top + "-"
			for k in spaces:
				top = top + "-"
			top = top + "+"
		top = top + "\n"
		full_string = full_string + top
		# indices
		top = " "
		for j in across:
			for k in spaces:
				top = top + " "
			top = top + str(j + 1)
			for k in range(self.spacing - len(str(j + 1)) + 1):
				top = top + " "
			top = top + " "
		top = top + "\n"
		full_string = full_string + top
		print(full_string)
		# for cell_row in range(self.row):
		# 	for cell_col in range(self.col):
		# 		a_cell = self.cells[cell_col][cell_row]
		# 		if a_cell.is_occupied():
		# 			print(a_cell.piece.get_player_type(), end=' ')
		# 		else:
		# 			print('O', end=' ')
		# 	print()


# b = Board(spacing=2)
# b.fill_board('X')
# b.add_piece(5, "R")
# b.add_piece(5, "B")
# b.add_piece(5, "R")
# b.add_piece(5, "R")
# b.add_piece(5, "B")
# b.add_piece(5, "B")
# b.print_board()
# print(b.is_board_full())
# print(b.is_move_allowed(3))
#print(str(b.cells[5][4].get_row()))
#print(b.row)
