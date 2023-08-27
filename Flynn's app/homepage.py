import tkinter as tk
import subprocess
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Footy Home")
window.geometry("360x640")

def prem_page():
    subprocess.Popen(['Python', 'premier-league.py'])
    #window.withdraw()

def laliga_page():
    subprocess.Popen(['Python', 'laliga.py'])
    #window.withdraw()

# Title Label
title_label = tk.Label(window, text="Footy Home", font=("Helvetica", 20))
title_label.pack(pady=30)

# Load the images for the buttons
laliga_image = Image.open('laliga 150x150 1 copy.jpg')
premier_image = Image.open('premier-league-logo copy.jpg')  # Replace with your actual image file
laliga_photo = ImageTk.PhotoImage(laliga_image)
premier_photo = ImageTk.PhotoImage(premier_image)

# Buttons with images
button_premier = tk.Button(window, image=premier_photo, command=prem_page)
button_premier.pack(pady=10)

button_laliga = tk.Button(window, image=laliga_photo, command=laliga_page)
button_laliga.pack(pady=10)

# Start the GUI event loop
window.mainloop()
