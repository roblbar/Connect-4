# Author: Robert L Barrera
# Class: CS474, Spring 2019
# Homework 4 : Main
# System: Windows 10
# April 1, 2019

from Board import Board
from GameController import Connect4Runner

debug_flag = False

if __name__ == "__main__":
    c4 = Connect4Runner()
    c4.play_game()
