import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Guessing Game")

# Set up the game
secret_number = random.randint(1, 100)
attempts = 0

# Define the game functions
def check_guess():
    global attempts
    guess = int(guess_entry.get())
    attempts += 1
    if guess == secret_number:
        result_label.config(text=f"Congratulations! You guessed the secret number in {attempts} attempts.")
        guess_entry.config(state="disabled")
        check_button.config(state="disabled")
    elif guess < secret_number:
        result_label.config(text="Your guess is too low. Guess again.")
    else:
        result_label.config(text="Your guess is too high. Guess again.")

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="")
    guess_entry.delete(0, tk.END)
    guess_entry.config(state="normal")
    check_button.config(state="normal")

# Create the game widgets
guess_label = tk.Label(root, text="Guess a number between 1 and 100:")
guess_label.pack(pady=10)

guess_entry = tk.Entry(root, width=10)
guess_entry.pack()

check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack(pady=10)

# Start the main loop
root.mainloop()






