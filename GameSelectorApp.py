import tkinter as tk
from tkinter import Frame, Button

class GameSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Selector")
        self.root.geometry("700x600")

        label = tk.Label(root, text="Pick Your Game!", font=("Arial", 18))
        label.pack(padx=20, pady=20)

        self.buttonframe = tk.Frame(root)
        self.buttonframe.pack(expand=True)

        self.buttonframe.columnconfigure(0, weight=1)

        self.choose_button_hangman = tk.Button(self.buttonframe, text="Hangman", font=("Arial", 16),
                                               command=self.show_hangman_game)
        self.choose_button_hangman.grid(row=0, column=0, padx=20, pady=20)

        self.choose_button_rps = tk.Button(self.buttonframe, text="Rock Paper Scissors", font=("Arial", 16),
                                           command=self.show_rps_game)
        self.choose_button_rps.grid(row=1, column=0, padx=20, pady=20)

        self.current_game_frame = None  # Placeholder for the current game frame

    def show_hangman_game(self):
        # Hide buttons when showing Hangman game
        self.choose_button_hangman.grid_forget()
        self.choose_button_rps.grid_forget()

        # Import and show Hangman game
        import hangman_game
        self.current_game_frame = hangman_game.HangmanGame(self.root)

    def show_rps_game(self):
        # Hide buttons when showing Rock Paper Scissors game
        self.choose_button_hangman.grid_forget()
        self.choose_button_rps.grid_forget()

        # Import and show Rock Paper Scissors game
        import rps_game
        self.current_game_frame = rps_game.RPSGame(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameSelectorApp(root)
    root.mainloop()
