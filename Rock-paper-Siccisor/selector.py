import tkinter as tk
from tkinter import messagebox
import random

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def make_choice(choice):
    global user_score, opponent_score
    opponent_choice = random.choice(['r', 'p', 's'])
    choices = {'r': 'Rock 🪨', 'p': 'Paper 📜', 's': 'Scissors ✂️'}
    user_choice = choices[choice]
    opponent_choice_text = choices[opponent_choice]

    result = ""
    if choice == opponent_choice:
        result = "It's a tie! 🤝"
    elif is_win(choice, opponent_choice):
        result = "You won! 🎉"
        user_score += 1
    else:
        result = "You lost! 😔"
        opponent_score += 1

    result_label.config(text=f"You chose {user_choice}\n{opponent} chose {opponent_choice_text}\n{result}")
    score_label.config(text=f"You: {user_score} - {opponent_score} {opponent}")
    if user_score >= 5:
        messagebox.showinfo("Game Over", "Congratulations! You reached 5 points first and won the game!")
    elif opponent_score >= 5:
        messagebox.showinfo("Game Over", f"{opponent} reached 5 points first. You lost the game.")

def selector():
    friends = ['Krishiv', 'Sneha', 'Ishaan', 'Dwija', 'Urja', 'Urva', 'Aarya', 'Mahin', 'Suhanee']
    return random.choice(friends)

# Main
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

user_score = 0
opponent_score = 0
opponent = selector()

title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 24, "bold"))
title_label.pack(pady=10)

score_label = tk.Label(root, text=f"You {user_score} - {opponent_score} {opponent}", font=("Arial", 18))
score_label.pack(pady=10)

result_label = tk.Label(root, text="Make your choice!", font=("Arial", 16))
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock 🪨", font=("Arial", 14), command=lambda: make_choice('r'))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(button_frame, text="Paper 📜", font=("Arial", 14), command=lambda: make_choice('p'))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors ✂️", font=("Arial", 14), command=lambda: make_choice('s'))
scissors_button.pack(side=tk.LEFT, padx=10)

root.mainloop()