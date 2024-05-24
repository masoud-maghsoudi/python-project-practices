"""
    In this script I have written a Tic Tac Toe Game with OOP.
    
    Author: Masoud Maghsoudi
    Github: https://github.com/masoud-maghsoudi
    Email:  masoud_maghsoudi@yahoo.com
"""

import tic_tac_toe as ttt


def main() -> None:
    """start a game and process it for a single round of game"""
    game = ttt.tic_tac_toe()
    game.select_sides()
    print(f"Your ID is {game.player_id} and PC ID is {game.pc_id}", end="\n \n")
    print(f"{game.token} is starting the game!", end="\n \n")

    while game.winner_check() == 0:
        if game.board_is_full() is True:
            print(game.board, end="\n \n")
            print("GAME IS OVER FOR NOW")
            return None
        print(game.board)
        if game.token == game.player_id:
            game.player_turn()
        else:
            game.pc_turn()

    print(game.board, end="\n \n")
    print(f'Winner is "{game.winner_check()}"')


if __name__ == "__main__":
    main()
