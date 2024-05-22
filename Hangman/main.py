"""
In this script I have written a Hangman Game with OOP
"""

import random


class Hangman:
    words = []
    target_word = []
    user_word = []
    penalty_numbers = 0

    def __init__(self):
        """
        This method fetches the Hangman words from words.txt file
        """
        with open("words.txt", "r", encoding="UTF-8") as file:
            for line in file:
                self.words.append(line.strip().lower())

    def new_game(self):
        """Select a random word for target_words from the word list"""
        self.target_word = random.choice(list(self.words))
        for ch in self.target_word:
            self.user_word.append("-")
        self.penalty_numbers = 0

    def check_guess(self, char: str) -> bool:
        """
        checks whether guessed character is in the target word or not

        Args:
            char (str): Guessed character

        Returns:
            bool: return True if guessed character is in target_word
        """
        return char in self.target_word

    def update_game_status(self, char: str):
        """update user_word according user guess

        Args:
            char (str): user guessed character
        """
        if self.check_guess(char):
            for i in range(len(self.target_word)):
                if char == self.target_word[i]:
                    self.user_word[i] = char
        else:
            self.penalty_numbers += 1

    def accomplished(self) -> bool:
        """Checks whether user accomplished in the game or not

        Returns:
            bool: returns True if user successfully accomplished the game
        """
        return self.user_word == list(self.target_word)

    def hanged(self):
        """Checks whether user lost the game or not

        Returns:
            bool: returns True if user lost the game
        """
        return self.penalty_numbers >= len(self.target_word)

    def endgame_check(self):
        """Checks whether the game is ended or not

        Returns:
            bool: returns True if user successfully accomplished the game
        """
        if self.accomplished():
            print(
                f'Congratulatinos, Your are the Winner!, The word is "{self.target_word}"',
                end="\n \n",
            )
        if self.hanged():
            print(
                f'Sorry, You Lost!. The word was "{self.target_word}", maybe next time!',
                end="\n \n",
            )


game = Hangman()
game.new_game()

while not game.hanged():
    if game.accomplished():
        break
    print(
        f"you have {len(game.target_word)-game.penalty_numbers} opportubities left to guess",
        end="\n \n",
    )
    print(" ".join(game.user_word), end="\n \n")
    user_guess = input("Input your guess: ").lstrip().lower()[0]
    game.update_game_status(user_guess)
    game.endgame_check()
