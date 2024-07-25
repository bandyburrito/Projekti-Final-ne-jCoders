import tkinter as tk
from tkinter import Frame, Button, Label
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
    

        self.computer_value = {
            "0": "Rock",
            "1": "Paper",
            "2": "Scissor"
        }

        self.create_ui()

    def create_ui(self):
        # Labels for player and computer choices
        self.label_player = Label(self.root, text="Player              ", font=10)
        self.label_player.pack()

        self.label_vs = Label(self.root, text="VS             ", font="normal 10 bold")
        self.label_vs.pack()

        self.label_computer = Label(self.root, text="Computer", font=10)
        self.label_computer.pack()

        # Label for displaying result
        self.label_result = Label(self.root, text="", font="normal 20 bold", bg="white", width=15,
                                  borderwidth=2, relief="solid")
        self.label_result.pack(pady=20)

        # Frame for buttons
        self.frame_buttons = Frame(self.root)
        self.frame_buttons.pack()

        # Buttons for rock, paper, and scissors
        self.button_rock = Button(self.frame_buttons, text="Rock", font=10, width=7, command=self.is_rock)
        self.button_rock.pack(side=tk.LEFT, padx=10)

        self.button_paper = Button(self.frame_buttons, text="Paper", font=10, width=7, command=self.is_paper)
        self.button_paper.pack(side=tk.LEFT, padx=10)

        self.button_scissor = Button(self.frame_buttons, text="Scissor", font=10, width=7, command=self.is_scissor)
        self.button_scissor.pack(padx=10)

        # Button to reset the game
        self.button_reset = Button(self.root, text="Reset Game", font=10, fg="red", bg="black", command=self.reset_game)
        self.button_reset.pack(pady=20)

    def is_rock(self):
        self.evaluate_game("Rock")

    def is_paper(self):
        self.evaluate_game("Paper")

    def is_scissor(self):
        self.evaluate_game("Scissor")

    def evaluate_game(self, player_choice):
        computer_choice = self.computer_value[str(random.randint(0, 2))]
        if computer_choice == player_choice:
            result_text = "Match Draw"
        elif (computer_choice == "Rock" and player_choice == "Scissor") or \
             (computer_choice == "Paper" and player_choice == "Rock") or \
             (computer_choice == "Scissor" and player_choice == "Paper"):
            result_text = "Computer Win"
        else:
            result_text = "Player Win"

        self.label_result.config(text=result_text)
        self.label_player.config(text=f"Player: {player_choice}")
        self.label_computer.config(text=f"Computer: {computer_choice}")

    def reset_game(self):
        self.label_result.config(text="")
        self.label_player.config(text="Player              ")
        self.label_computer.config(text="Computer")

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGame(root)
    root.mainloop()
