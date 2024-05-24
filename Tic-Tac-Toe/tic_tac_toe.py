"""
    Class Implementation of Tic Tac Toe Game
    
    Author: Masoud Maghsoudi
    Github: https://github.com/masoud-maghsoudi
    Email:  masoud_maghsoudi@yahoo.com
"""

import random
from time import sleep
import numpy as np


class tic_tac_toe:
    """A Class to represent a Tic Tac Toe game.

    Methods:
        new_game: None
            Generates a new turn for game
        row_win: bool
            Checks the board for row win condition
        col_win: bool
            Checks the board for column win condition
        diag_win: bool
            Checks the board for diagonal win condition
        winner_check: int
            checks whether any of players has the winning condition and return its ID
        vacant_cells: list
            returns the list of the board vacant cells
        select_sides: none
            selects random IDs and assign them to the player and machine
        board_is_full: bool
            checks whether the game board is full or not
        cell_is_empty: bool
            checks whether the given cell of the board is empty or not
        player_cell_select: tuple
            gets player input and verifys it to select a cell by player and return the tuple of the verfied input
        player_turn: none
            processes the player turn to select a cell
        pc_turn: none
            processes the pc turn to select a cell

    Attributes:
        players: determines the list of possible IDs for players
        player_id: ID given to the player in the game
        pc_id: ID given to the machine in the game
        token: Token ID for keeping the ID of player in each turn


    """

    players = (1, 2)
    player_id = 0
    pc_id = 0
    token = 0

    def __init__(self):
        """initiates a class object"""
        self.board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.token = random.choice(self.players)

    def __str__(self):
        """class string

        Returns:
            str: class description
        """
        return "creates a board for Tic Tac Toe"

    def new_game(self):
        """generates a new empty board for game"""
        self.board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.token = random.choice(self.players)

    def row_win(self, player: int) -> bool:
        """Checks the board for row win condition

        Args:
            player (int): ID of the player to check

        Returns:
            bool: check result
        """
        for row in self.board:
            if row[0] == row[1] == row[2] == player:
                return True
        return False

    def col_win(self, player_id: int) -> bool:
        """Checks the board for column win condition

        Args:
            player (int): ID of the player to check

        Returns:
            bool: check result
        """
        for i in range(3):
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2] == player_id:
                return True
        return False

    def diag_win(self, player: int) -> bool:
        """Checks the board for diagonal win condition

        Args:
            player (int): ID of the player to check

        Returns:
            bool: check result
        """
        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] == player:
            return True
        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] == player:
            return True
        return False

    def winner_check(self) -> int:
        """checks whether any of players has the winning condition and return its ID

        Returns:
            int: ID of the winner
        """
        for player in self.players:
            if self.row_win(player) is True:
                return player
            if self.col_win(player) is True:
                return player
            if self.diag_win(player) is True:
                return player
        return 0

    def vacant_cells(self) -> list:
        """returns the list of the board vacant cells

        Returns:
            list: vacant cells
        """
        x = np.where(self.board == 0)
        return list(zip(x[0], x[1]))

    def select_sides(self) -> None:
        """selects random IDs and assign them to the player and machine"""
        self.player_id = random.choice(self.players)
        self.pc_id = 1 if self.player_id == 2 else 2

    def board_is_full(self) -> bool:
        """checks whether the game board is full or not

        Returns:
            bool: check result
        """
        return False if 0 in self.board else True

    def cell_is_empty(self, i: int, j: int) -> bool:
        """checks whether the given cell of the board is empty or not

        Args:
            i (int): X-axis of cell coordinates
            j (int): Y-axis of cell coordinates

        Returns:
            bool: check result
        """
        return True if (i - 1, j - 1) in self.vacant_cells() else False

    def player_cell_select(self) -> tuple:
        """gets player input and verifys it to select a cell by player and return the tuple of the verfied input

        Returns:
            tuple: coordinates of player selected cell
        """
        selected = False

        while selected is not True:
            try:
                x_input = int(
                    input("Please choose X-axis of cell (1 or 2 or 3): ").strip()[0]
                )
                y_input = int(
                    input("Please choose Y-axis of cell (1 or 2 or 3): ").strip()[0]
                )
            except (IndexError, TypeError, ValueError):
                print("Input is invalid, Please try again")
                continue

            if x_input > 3 or x_input < 1 or y_input > 3 or y_input < 1:
                print("Input is out of range, Please try agian")
                continue

            if self.cell_is_empty(x_input, y_input) is not True:
                print("This cell is already filled, Please select a vacant cell")
                continue
            selected = True
        return x_input - 1, y_input - 1

    def player_turn(self):
        """processes the player turn to select a cell"""
        i, j = self.player_cell_select()
        self.board[i, j] = self.player_id
        self.token = self.pc_id

    def pc_turn(self):
        """processes the pc turn to select a cell"""
        i, j = random.choice(self.vacant_cells())
        self.board[i, j] = self.pc_id
        self.token = self.player_id
        sleep(1)
        print("\n Your Turn", end="\n \n")
