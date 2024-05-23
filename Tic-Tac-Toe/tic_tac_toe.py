import random
from time import sleep
import numpy as np


class tic_tac_toe:
    players = (1, 2)
    player_id = 0
    pc_id = 0
    token = 0

    def __init__(self):
        self.board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.token = random.choice(self.players)

    def __str__(self):
        return "creates a board for Tic Tac Toe"

    def new_game(self):
        """
        docstring
        """
        self.board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.token = random.choice(self.players)

    def row_win(self, player: int) -> bool:
        for row in self.board:
            if row[0] == row[1] == row[2] == player:
                return True
        return False

    def col_win(self, player_id: int) -> bool:
        for i in range(3):
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2] == player_id:
                return True
        return False

    def diag_win(self, player: int) -> bool:
        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] == player:
            return True
        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] == player:
            return True
        return False

    def winner_check(self) -> int:
        """
        docstring
        """
        for player in self.players:
            if self.row_win(player) is True:
                return player
            if self.col_win(player) is True:
                return player
            if self.diag_win(player) is True:
                return player
        return 0

    def board_is_full(self) -> bool:
        """
        docstring
        """
        # print(np.where(self.board == 0))
        # return not np.where(self.board == 0)
        return False if 0 in self.board else True

    def select_sides(self) -> None:
        """_summary_"""
        self.player_id = random.choice(self.players)
        self.pc_id = 1 if self.player_id == 2 else 2

    def cell_is_empty(self, i: int, j: int) -> bool:
        """
        docstring
        """
        return True if (i - 1, j - 1) in self.vacant_cells() else False

    def player_select_cell(self) -> tuple:
        """
        docstring
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
        """
        docstring
        """
        i, j = self.player_select_cell()
        self.board[i, j] = self.player_id
        self.token = self.pc_id

    def vacant_cells(self) -> list:
        """
        docstring
        """
        x = np.where(self.board == 0)
        return list(zip(x[0], x[1]))

    def pc_turn(self):
        """
        docstring
        """
        i, j = random.choice(self.vacant_cells())
        self.board[i, j] = self.pc_id
        self.token = self.player_id
        sleep(1)
        print("\n Your Turn", end="\n \n")
