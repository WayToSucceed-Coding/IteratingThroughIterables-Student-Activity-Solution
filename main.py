import random
import tkinter as tk
from tkinter import messagebox

# Initialize the game state
word_list = ["python", "development", "hangman", "challenge", "programming"]
word = random.choice(word_list)
guessed_letters = []
attempts = 6 #Debug 2
display_word = " _ " * len(word)

# Function to update the display word
def update_word_display():
    global display_word
    new_display = ""
    for i in word: 
        if i in guessed_letters: #Debug 1
            new_display += ' '+i
        else:
            new_display += " _ "
    display_word = new_display
    word_label.config(text=display_word)

# Function to check the user's guess
def check_guess():
    global attempts
    guess = guess_entry.get().lower() #Debug 3

    # Ensure the guess is a single letter and not guessed before
    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if guess in guessed_letters:
        messagebox.showinfo("Already Guessed", f"You've already guessed the letter '{guess}'.")
        return

    # Add the guess to the guessed letters list
    guessed_letters.append(guess)

    # Check if the guess is in the word
    if guess in word:
        update_word_display()
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts left: {attempts}")
        messagebox.showinfo("Incorrect Guess", f"The letter '{guess}' is not in the word.")

    # Check for game over or win
    if attempts == 0:
        messagebox.showerror("Game Over", f"Game Over! The word was '{word}'.")
        root.quit()
    elif ''.join( display_word.split(' ')) == word:
        messagebox.showinfo("You Win!", "Congratulations! You've guessed the word!")
        root.quit()

    # Clear the guess entry for the next guess
    guess_entry.delete(0, tk.END)

# Set up the main Tkinter window
root = tk.Tk()
root.title("Hangman Game")

# Set a fixed window size
root.geometry("400x400")
root.resizable(False, False)  # Prevent window resizing

# Set a nice background color
root.config(bg="#f2f2f2")

# Display the hidden word
word_label = tk.Label(root, text=display_word, font=("Helvetica", 24), bg="#f2f2f2", fg="#333333")
word_label.pack(pady=20)

# Entry field for guessing letters
guess_entry = tk.Entry(root, font=("Helvetica", 18), width=5)
guess_entry.pack(pady=10)

# Button to submit the guess
guess_button = tk.Button(root, text="Guess", font=("Helvetica", 14), command=check_guess, bg="#4CAF50", fg="white", relief="solid", width=15)
guess_button.pack(pady=10)

# Label to display the remaining attempts
attempts_label = tk.Label(root, text=f"Attempts left: {attempts}", font=("Helvetica", 14), bg="#f2f2f2", fg="#333333")
attempts_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
