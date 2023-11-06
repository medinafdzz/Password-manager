import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import jwt
import re
import psycopg2
import os

# Create the main window
window = tk.Tk()
window.title("Password Manager")
window.geometry("375x175")
window.resizable(False, False)
window.iconbitmap("icon.ico")

# Set background and font colors
bg_color = "#36393F"
fg_color = "white"
font_style = "Arial"
font_size = 10

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

# Modify the save_password_to_db function to get the username and password from the input fields


def save_password_to_db():

    # Get the password from the environment variable
    passwordDB = os.environ.get("DB_PASSWORD")

    if passwordDB is None:
        messagebox.showerror(
            "Error", "Database password not configured in the environment variable")
        return

    username = username_entry.get()
    password = password_entry.get()

    # Replace these data with your own values
    try:
        connection = psycopg2.connect(
            user="postgres",
            password=passwordDB,  # or change passwordDB for your password
            host="localhost",
            port="5432",
            database="Password-Manager"
        )
        cursor = connection.cursor()
        token = generate_token(username, password)
        cursor.execute(
            "INSERT INTO passwords (username, password,token) VALUES (%s, %s,%s)", (username, password, token))
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Credentials saved successfully.")
    except Exception as e:
        messagebox.showerror(
            "Error", "Error saving credentials to the database: " + str(e))


# Create a frame for the buttons
button_frame = tk.Frame(window, bg=bg_color)
button_frame.pack()

# Function to decrypt a token with a custom dialog


def decrypt_token():
    dialog = tk.simpledialog.askstring(
        "Decrypt Token", "Enter Token:", parent=window, show="*")
    if dialog is not None:
        try:
            decoded_token = jwt.decode(
                dialog, secret_key, algorithms=['HS256'])
            username = decoded_token['username']
            password = decoded_token['password']
            messagebox.showinfo("Decrypted Token",
                                f"Username: {username}\nPassword: {password}")
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
                    decoded_token = jwt.decode(
                        token, secret_key, algorithms=['HS256'])
                    username = decoded_token['username']
                    password = decoded_token['password']
                    messagebox.showinfo(
                        "Decrypted Token", f"Username: {username}\nPassword: {password}")
                except Exception as e:
                    messagebox.showerror(
                        "Error", "Error decrypting the token.")
            else:
                messagebox.showerror("Error", "Token not found in the file.")


# Label for the username
username_label = tk.Label(window, text="Username:",
                          bg=bg_color, fg=fg_color, font=(font_style, font_size))
username_label.pack()

# Entry field for the username
username_entry = tk.Entry(window, bg="white", highlightbackground=bg_color,
                          highlightthickness=1, font=(font_style, font_size))
username_entry.pack()

# Label for the password
password_label = tk.Label(window, text="Password:",
                          bg=bg_color, fg=fg_color, font=(font_style, font_size))
password_label.pack()

# Entry field for the password
password_entry = tk.Entry(window, show="*", bg="white", highlightbackground=bg_color,
                          highlightthickness=1, font=(font_style, font_size))
password_entry.pack()

# Space between the password entry and the buttons
space_frame = tk.Frame(window, height=10, bg=bg_color)
space_frame.pack()

# Create a frame for buttons
button_frame = tk.Frame(window, bg=bg_color)
button_frame.pack()

# Button to decrypt a token with a custom dialog
decrypt_button = tk.Button(button_frame, text="Reveal token", command=decrypt_token, bg=bg_color,
                           fg=fg_color, highlightbackground=bg_color, highlightthickness=0, font=(font_style, font_size))
# Añade un espacio horizontal de 10 píxeles a la derecha del botón Decrypt Token
decrypt_button.pack(side=tk.LEFT, padx=5)

# Create an invisible frame for spacing on the right
invisible_frame = tk.Frame(button_frame, width=14, bg=bg_color)
invisible_frame.pack(side=tk.RIGHT)

# Button to load and decrypt a token from a file
load_decrypt_button = tk.Button(button_frame, text="Load Token", command=load_and_decrypt_token, bg=bg_color,
                                fg=fg_color, highlightbackground=bg_color, highlightthickness=0, font=(font_style, font_size))
load_decrypt_button.pack(side=tk.RIGHT)


# Space between the password entry and the buttons
space_frame = tk.Frame(window, height=10, bg=bg_color)
space_frame.pack()

# Create a frame for buttons
button_frame = tk.Frame(window, bg=bg_color)
button_frame.pack()


# Button to save the password and token to a text file
save_button = tk.Button(button_frame, text="Save Credentials", command=save_password_to_db, bg=bg_color,
                        fg=fg_color, highlightbackground=bg_color, highlightthickness=0, font=(font_style, font_size))
save_button.pack(side=tk.RIGHT, padx=5)

# Button to save the password and token to the database
save_db_button = tk.Button(button_frame, text="Save to Database", command=save_password_to_db, bg=bg_color,
                           fg=fg_color, highlightbackground=bg_color, highlightthickness=0, font=(font_style, font_size))
save_db_button.pack(side=tk.LEFT)


# Center the window on the screen
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (window_width // 2)
y = (window.winfo_screenheight() // 2) - (window_height // 2)
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

window.mainloop()
