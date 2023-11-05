import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import jwt
import re

# Create the main window
window = tk.Tk()
window.title("Password Manager")
window.geometry("400x180")  # Window size

# No resizable window
window.resizable(False, False)

# Set the window icon
window.iconbitmap('icon.ico')

# Configure a background color and font
bg_color = "#36393F"  # Dark gray background color
fg_color = "white"    # White text color
font_style = "Arial"  # Font style
font_size = 10        # Font size

# Set the background color of the window
window.configure(bg=bg_color)

# Secret key to verify the token
secret_key = 'my_secret_key'

# Function to generate a token
def generate_token(username, password):
    payload = {
        'username': username,
        'password': password
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

# Function to save the password and token to a text file
def save_password():
    username = username_entry.get()
    password = password_entry.get()

    if not any(c.isalpha() for c in username):
        # Check if there is at least one letter in the username
        messagebox.showerror("Error", "The username must contain at least one letter.")
    elif len(password) < 5:
        # Show a popup window with a warning message
        messagebox.showerror("Error", "The password must be at least 5 characters long.")
    else:
        # Generate the token
        token = generate_token(username, password)

        # Open a file dialog to choose the file location
        saved_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

        if saved_file:
            with open(saved_file, "w") as file:
                file.write(f"Username: {username}\nToken: {token}")
                messagebox.showinfo("Success", "Credentials saved successfully.")  # Confirmation message

        # Clear the fields after saving
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# Function to decrypt a token with a custom dialog
def decrypt_token():
    dialog = tk.simpledialog.askstring("Decrypt Token", "Enter Token:", parent=window, show="*")
    if dialog is not None:
        try:
            decoded_token = jwt.decode(dialog, secret_key, algorithms=['HS256'])
            username = decoded_token['username']
            password = decoded_token['password']
            messagebox.showinfo("Decrypted Token", f"Username: {username}\nPassword: {password}")
        except Exception as e:
            messagebox.showerror("Error", "Error decrypting the token.")

# Function to load and decrypt a token from a file
def load_and_decrypt_token():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            token_match = re.search(r"Token:\s*(\S+)", content)
            if token_match:
                token = token_match.group(1)
                try:
                    decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
                    username = decoded_token['username']
                    password = decoded_token['password']
                    messagebox.showinfo("Decrypted Token", f"Username: {username}\nPassword: {password}")
                except Exception as e:
                    messagebox.showerror("Error", "Error decrypting the token.")
            else:
                messagebox.showerror("Error", "Token not found in the file.")

# Label for the username
username_label = tk.Label(window, text="Username:", bg=bg_color, fg=fg_color, font=(font_style, font_size))
username_label.pack()

# Entry field for the username
username_entry = tk.Entry(window, bg="white", highlightbackground=bg_color, highlightthickness=1, font=(font_style, font_size))
username_entry.pack()

# Label for the password
password_label = tk.Label(window, text="Password:", bg=bg_color, fg=fg_color, font=(font_style, font_size))
password_label.pack()

# Entry field for the password
password_entry = tk.Entry(window, show="*", bg="white", highlightbackground=bg_color, highlightthickness=1, font=(font_style, font_size))
password_entry.pack()

# Space between the password entry and the buttons
space_frame = tk.Frame(window, height=10, bg=bg_color)
space_frame.pack()

# Create a frame for buttons
button_frame = tk.Frame(window, bg=bg_color)
button_frame.pack()

# Button to save the password and token to a text file
save_button = tk.Button(button_frame, text="Save Credentials", command=save_password, bg=bg_color, fg=fg_color, highlightbackground=bg_color, highlightthickness=0, font=(font_style, font_size))
save_button.pack(side=tk.TOP)

# Create another space frame
space_frame = tk.Frame(button_frame, height=10, bg=bg_color)
space_frame.pack()

# Button to decrypt a token with a custom dialog
decrypt_button = tk.Button(button_frame, text="Decrypt Token", command=decrypt_token, bg=bg_color, fg=fg_color, highlightbackground=bg_color, highlightthickness=0, font=(font_style, font_size))
decrypt_button.pack(side=tk.LEFT, padx=5)  # Añade un espacio horizontal de 10 píxeles a la derecha del botón Decrypt Token

# Button to load and decrypt a token from a file
load_decrypt_button = tk.Button(button_frame, text="Load Token", command=load_and_decrypt_token, bg=bg_color, fg=fg_color, highlightbackground=bg_color, highlightthickness=0, font=(font_style, font_size))
load_decrypt_button.pack(side=tk.RIGHT)

# Center the window on the screen
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (window_width // 2)
y = (window.winfo_screenheight() // 2) - (window_height // 2)
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

window.mainloop()
