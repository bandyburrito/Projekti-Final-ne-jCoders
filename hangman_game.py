import tkinter as tk
from tkinter import Label, Entry, Button
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("300x600")

        self.words = ['python', 'programming', 'tutorial', 'hangman', 'algorithm', 'syntax']

        self.hangman_art = [
            "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
        ]

        self.choose_word()
        self.create_ui()

    def choose_word(self):
        self.word = random.choice(self.words)
        self.word_with_blanks = '_' * len(self.word)

    def create_ui(self):
        # Hangman image display
        self.hangman_label = tk.Label(self.root, font=("Courier", 16))
        self.hangman_label.pack(padx=20)

        # Word to guess display
        self.word_label = tk.Label(self.root, text=self.word_with_blanks, font=("Arial", 24))
        self.word_label.pack(padx=20)

        # Entry for guessing
        self.guess_entry = tk.Entry(self.root, width=7, font=("Arial", 24))
        self.guess_entry.pack(padx=20)

        # Guess button
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess, font=("Arial", 16))
        self.guess_button.pack(padx=20)

        # Result display
        self.result_label = tk.Label(self.root, font=("Arial", 24))
        self.result_label.pack(padx=20)

        self.mistakes = 0
        self.update_hangman()

    def update_hangman(self):
        self.hangman_label.config(text=self.hangman_art[self.mistakes])

    def check_guess(self):
        guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)

        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_with_blanks = self.word_with_blanks[:i] + guess + self.word_with_blanks[i+1:]
            self.word_label.config(text=self.word_with_blanks)
            if '_' not in self.word_with_blanks:
                self.end_game("win")
        else:
            self.mistakes += 1
            self.update_hangman()
            if self.mistakes == 6:
                self.end_game("lose")

    def end_game(self, result):
        if result == "win":
            result_text = "YOU WIN!"
        else:
            result_text = f"You Lose, the word was: {self.word}"
        self.result_label.config(text=result_text)
        self.guess_entry.config(state="disabled")
        self.guess_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()
