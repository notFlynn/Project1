import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import bcrypt

BACKGROUND_IMAGE_PATH = "stadium_export_3.jpg"

# Function to set the background image of a window
def set_background_image(window, image_path):
    bg_image = ImageTk.PhotoImage(Image.open(image_path))
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    return bg_image

# Function to create the login window
def login_window():
    window = tk.Tk()
    window.title("Footy Stats Login")
    window.geometry("360x640")

    bg_image = set_background_image(window, BACKGROUND_IMAGE_PATH)

    title_label = tk.Label(window, text="Welcome to Footy Stats!", font=("Arial", 24, "bold"), fg="#3498db")
    title_label.pack(pady=20)

    username_entry = tk.Entry(window, width=30)
    password_entry = tk.Entry(window, show="*", width=30)

    username_label = tk.Label(window, text="Username")
    password_label = tk.Label(window, text="Password")

    username_label.pack()
    username_entry.pack(pady=5)
    password_label.pack()
    password_entry.pack(pady=5)

    submit_button = tk.Button(window, text="Submit", highlightthickness=0, bd=0, borderwidth=0, bg="#e1e1e1", relief="flat")
    submit_button.pack(pady=10)

    def submit_login():
        username = username_entry.get()
        password = password_entry.get()

        if not username:
            messagebox.showerror("Error", "Please enter a username")
            return
        if not password:
            messagebox.showerror("Error", "Please enter a password")
            return

        with open("users.txt", "r") as f:
            for line in f:
                user = line.strip().split(",")
                if len(user) >= 2 and user[0] == username and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
                    window.destroy()

                    project_root = os.path.dirname(os.path.abspath(__file__))
                    os.chdir(project_root)
                    exec(open("homepage.py").read())
                    return

        messagebox.showerror("Error", "Invalid username or password")

    submit_button.config(command=submit_login)

    switch_button = tk.Button(window, text="Sign up here")
    switch_button.pack(pady=5)

    def switch_to_signup():
        window.destroy()
        signup_window()

    switch_button.config(command=switch_to_signup)

    window.mainloop()

# Function to create the sign-up window
def signup_window():
    window = tk.Tk()
    window.title("Sign up")
    window.geometry("360x640")

    bg_image = set_background_image(window, BACKGROUND_IMAGE_PATH)

    title_label = tk.Label(window, text="Sign up", font=("Arial", 20))
    title_label.pack(pady=20)

    username_entry = tk.Entry(window, width=30)
    password_entry = tk.Entry(window, show="*", width=30)
    password_verify_entry = tk.Entry(window, show="*", width=30)

    username_label = tk.Label(window, text="Username")
    password_label = tk.Label(window, text="Password")
    password_verify_label = tk.Label(window, text="Verify Password")

    username_label.pack()
    username_entry.pack(pady=5)
    password_label.pack()
    password_entry.pack(pady=5)
    password_verify_label.pack()
    password_verify_entry.pack(pady=5)

    submit_button = tk.Button(window, text="Submit")
    submit_button.pack(pady=10)

    def submit_signup():
        username = username_entry.get()
        password = password_entry.get()

        if not username:
            messagebox.showerror("Error", "Please enter a username")
            return
        if not password:
            messagebox.showerror("Error", "Please enter a password")
            return
        if password != password_verify_entry.get():
            messagebox.showerror("Error", "Passwords do not match")
            return
        if len(password) < 8 or not any(char.isdigit() for char in password) or \
           not any(char.isupper() for char in password) or not any(char.islower() for char in password):
            messagebox.showerror("Error", "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit")
            return

        with open("users.txt", "r") as f:
            for line in f:
                user = line.strip().split(",")
                if len(user) >= 1 and user[0] == username:
                    messagebox.showerror("Error", "Username already exists")
                    return

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with open("users.txt", "a") as f:
            f.write(username + "," + hashed_password + "\n")

        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        password_verify_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "You have successfully signed up")

    submit_button.config(command=submit_signup)

    switch_button = tk.Button(window, text="Back to Login")
    switch_button.pack(pady=5)

    def switch_to_login():
        window.destroy()
        login_window()

    switch_button.config(command=switch_to_login)

    window.mainloop()

# Start the login window when the script is run
login_window()
