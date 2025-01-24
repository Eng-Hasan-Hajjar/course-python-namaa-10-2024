import tkinter as tk
from tkinter import messagebox

def decide_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    if (choice1 == "rock" and choice2 == "scissor") or \
       (choice1 == "paper" and choice2 == "rock") or \
       (choice1 == "scissor" and choice2 == "paper"):
        return "Player 1 wins!"
    return "Player 2 wins!"

def play_game():
    choice1 = player1_choice.get().lower()
    choice2 = player2_choice.get().lower()

    if choice1 not in ["rock", "paper", "scissor"] or choice2 not in ["rock", "paper", "scissor"]:
        messagebox.showerror("Invalid Input", "Please enter rock, paper, or scissor.")
        return

    result = decide_winner(choice1, choice2)
    messagebox.showinfo("Result", f"Player 1: {choice1}\nPlayer 2: {choice2}\n\n{result}")


root = tk.Tk()
root.title("Rock, Paper, Scissors")


player1_label = tk.Label(root, text="Player 1: Enter rock, paper, or scissors")
player1_label.pack()
player1_choice = tk.Entry(root)
player1_choice.pack()



player2_label = tk.Label(root, text="Player 2: Enter rock, paper, or scissor")
player2_label.pack()
player2_choice = tk.Entry(root)
player2_choice.pack()


play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()


root.mainloop()