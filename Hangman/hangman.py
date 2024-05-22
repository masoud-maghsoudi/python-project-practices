"""
This is a class module for Hangman Game

"""

from random import choice


class Hangman:
    words = []
    __target_word = []
    user_word = []
    __penalty_counter = 0

    def __str__(self) -> str:
        return "Select a word to be guessed by gamer"

    def __init__(self):
        """
        Initiates a Hangman game
        """
        with open("words.txt", "r", encoding="UTF-8") as file:
            for line in file:
                self.words.append(line.strip().lower())

    def new_game(self):
        """Select a random word for target_words from the word list"""
        self.__target_word = choice(list(self.words))
        self.user_word.clear()
        for ch in self.__target_word:
            self.user_word.append("-")
        self.__penalty_counter = 0

    def check_guess(self, char: str) -> bool:
        """
        checks whether guessed character is in the target word or not

        Args:
            char (str): Guessed character

        Returns:
            bool: return True if guessed character is in target_word
        """
        return char in self.__target_word

    def update_game_status(self, char: str):
        """update user_word according user guess

        Args:
            char (str): user guessed character
        """
        if self.check_guess(char):
            for i in range(len(self.__target_word)):
                if char == self.__target_word[i]:
                    self.user_word[i] = char
        else:
            self.__penalty_counter += 1

    def accomplished(self) -> bool:
        """Checks whether user accomplished in the game or not

        Returns:
            bool: returns True if user successfully accomplished the game
        """
        return self.user_word == list(self.__target_word)

    def hanged(self):
        """Checks whether user lost the game or not

        Returns:
            bool: returns True if user lost the game
        """
        return self.__penalty_counter >= len(self.__target_word)

    def endgame_check(self):
        """Checks whether the game is ended or not

        Returns:
            bool: returns True if user successfully accomplished the game
        """
        if self.accomplished():
            print(
                f'Congratulatinos, Your are the Winner!, The word is "{self.__target_word}"',
                end="\n \n",
            )
        if self.hanged():
            print(
                f'Sorry, You Lost!. The word was "{self.__target_word}", maybe next time!',
                end="\n \n",
            )
    def guess_left_count(self) -> int:
        """returns number of opportunities left to guess

        Returns:
            int: number of opportunities left to guess
        """
        return len(self.__target_word)-self.__penalty_counter
