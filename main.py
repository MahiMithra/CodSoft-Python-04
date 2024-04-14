import tkinter as tk
import random

# Function to get computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'User wins'
    else:
        return 'Computer wins'

# Function to process a round
def play_round(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    update_display(user_choice, computer_choice, result)

# Function to update the display
def update_display(user_choice, computer_choice, result):
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")
    
    if result == 'User wins':
        score['user'] += 1
    elif result == 'Computer wins':
        score['computer'] += 1
    
    score_label.config(text=f"Score - You: {score['user']}, Computer: {score['computer']}")

# Creating the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Color themes
background_color = "#232323"
text_color = "#ffffff"
button_color = "#4CAF50"
result_color = "#FFC107"

root.configure(bg=background_color)

# Initializing score dictionary
score = {'user': 0, 'computer': 0}

# Labels for choices and results
user_choice_label = tk.Label(root, text="Your Choice: ", font=('Helvetica', 14), bg=background_color, fg=text_color)
user_choice_label.pack(pady=(20, 10))

computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=('Helvetica', 14), bg=background_color, fg=text_color)
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=('Helvetica', 14, 'bold'), bg=background_color, fg=result_color)
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0, Computer: 0", font=('Helvetica', 14), bg=background_color, fg=text_color)
score_label.pack(pady=(10, 20))

# Buttons for user to select their choice
buttons_frame = tk.Frame(root, bg=background_color)
buttons_frame.pack(pady=(20, 10))

rock_button = tk.Button(buttons_frame, text="Rock", font=('Helvetica', 12), bg=button_color, fg=text_color, command=lambda: play_round('rock'))
rock_button.grid(row=0, column=0, padx=8, pady=10)

paper_button = tk.Button(buttons_frame, text="Paper", font=('Helvetica', 12), bg=button_color, fg=text_color, command=lambda: play_round('paper'))
paper_button.grid(row=0, column=1, padx=8, pady=10)

scissors_button = tk.Button(buttons_frame, text="Scissors", font=('Helvetica', 12), bg=button_color, fg=text_color, command=lambda: play_round('scissors'))
scissors_button.grid(row=0, column=2, padx=8, pady=10)

# Start the GUI
root.mainloop()

