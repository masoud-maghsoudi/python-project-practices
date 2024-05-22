"""
In this script I have written a Hangman Game with OOP
"""

import hangman as hm


def main():
    play = True
    game = hm.Hangman()
    game.new_game()

    while play:
        print(
            f"you have {game.guess_left_count()} opportubities left to guess",
            end="\n \n",
        )
        print(" ".join(game.user_word), end="\n \n")
        try:
            user_guess = input("Input your guess: ").lstrip().lower()[0]
        except IndexError:
            print("Your input is invalid, please try again")
            continue
        game.update_game_status(user_guess)
        game.endgame_check()
        if game.accomplished() or game.hanged():
            try:
                replay = input("Would you like to replay: ").lstrip().lower()[0]
            except IndexError:
                print("Goodbye, Have Fun!")
                play = False
                break
            if replay == "y":
                game.new_game()
            else:
                play = False
                print("Goodbye, Have Fun!")


if __name__ == "__main__":
    main()
