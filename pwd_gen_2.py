import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():

    """Generate a random password and display it in the UI."""
    try:
        length = int(entry_length.get())  # Get length from input field

        if length < 8:
            messagebox.showwarning("Invalid Input", "Password must be at least 8 characters long!")
            return
        
        # Get favorite words from input field
        favorite_words = entry_fav_words.get().strip().split(",")  # Split by commas
        favorite_words = [word.strip() for word in favorite_words if word.strip()]  # Remove spaces

        if not favorite_words:
            messagebox.showwarning("Invalid Input", "Enter at least one favorite word!")
            return
        
        # Pick a random favorite word
        chosen_word = random.choice(favorite_words)

        if len(chosen_word) > length:
            messagebox.showwarning("Too Long!", f"Favorite word '{chosen_word}' is longer than the password length!")
            return


        # Define character pool based on checkbox selections
        character_pool = ""
        if var_uppercase.get():
            character_pool += string.ascii_uppercase
        if var_numbers.get():
            character_pool += string.digits
        if var_special_chars.get():
            character_pool += string.punctuation
        character_pool += string.ascii_lowercase  # Always include lowercase letters

        if not character_pool:  # If no options are selected
            messagebox.showwarning("Invalid Selection", "Select at least one option for password generation!")
            return
        
        # Calculate remaining length for random characters (ensuring the favorite word is in the middle)
        remaining_length = length - len(chosen_word)

        # Generate random characters to fill the rest of the password
        left_random = ''.join(random.choice(character_pool) for _ in range(remaining_length // 2))
        right_random = ''.join(random.choice(character_pool) for _ in range(remaining_length - len(left_random)))

        # Combine random characters with the favorite word, ensuring the word is intact and visible
        password = left_random + chosen_word + right_random

        # Display the generated password
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
     
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")


def copy_to_clipboard():
    """Copy the generated password to the clipboard."""
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first!")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x450")
root.resizable(False, False)

# Title Label
label_title = tk.Label(root, text="Random Password Generator", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

# Password Length Input
frame_length = tk.Frame(root)
frame_length.pack(pady=5)
label_length = tk.Label(frame_length, text="Password Length:", font=("Arial", 12))
label_length.pack(side=tk.LEFT)
entry_length = tk.Entry(frame_length, font=("Arial", 12), width=5)
entry_length.pack(side=tk.LEFT, padx=5)

# Favorite Words Input
frame_fav_words = tk.Frame(root)
frame_fav_words.pack(pady=5)
label_fav_words = tk.Label(frame_fav_words, text="Favorite Words (comma-separated):", font=("Arial", 10))
label_fav_words.pack(side=tk.LEFT)
entry_fav_words = tk.Entry(root, font=("Arial", 10), width=35)
entry_fav_words.pack(pady=5)

# Checkboxes for character selection
var_uppercase = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_special_chars = tk.BooleanVar(value=True)

frame_checkboxes = tk.Frame(root)
frame_checkboxes.pack(pady=10)
chk_uppercase = tk.Checkbutton(frame_checkboxes, text="Include Uppercase (A-Z)", variable=var_uppercase, font=("Arial", 10))
chk_uppercase.pack(anchor="w")
chk_numbers = tk.Checkbutton(frame_checkboxes, text="Include Numbers (0-9)", variable=var_numbers, font=("Arial", 10))
chk_numbers.pack(anchor="w")
chk_special_chars = tk.Checkbutton(frame_checkboxes, text="Include Special Characters (@!#...)", variable=var_special_chars, font=("Arial", 10))
chk_special_chars.pack(anchor="w")

# Generate Password Button
btn_generate = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
btn_generate.pack(pady=10)

# Password Output Field
entry_password = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
entry_password.pack(pady=5)

# Copy to Clipboard Button
btn_copy = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard)
btn_copy.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
