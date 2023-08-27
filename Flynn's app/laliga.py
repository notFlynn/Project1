import csv
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import tkinter.font as tkFont
import sys




class LaLigaResultsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2020-2021 Results")  # Set the application title
        self.geometry("360x640")  # Set the window geometry

        self.teams = [
            "Athletic Club Bilbao", "FC Barcelona", "RC Celta Vigo", "Real Madrid", "Valencia CF", "Real Sociedad",
            "RCD Mallorca", "SD Eibar", "CD Leganés", "CA Osasuna", "Villarreal CF", "Granada CF",
            "Deportivo Alavés", "Levante UD", "RCD Espanyol", "Sevilla FC", "Real Betis", "Real Valladolid CF",
            "Atlético Madrid", "Getafe CF"
        ]

        self.week_var = tk.StringVar()
        self.team_var = tk.StringVar()
        self.select_all_var = tk.BooleanVar()


        # Load the background image
        background_image_path = os.path.join(os.path.dirname(__file__), "footy pitch copy.jpeg")
        background_img = Image.open(background_image_path)
        self.background_img = ImageTk.PhotoImage(background_img)

        # Create a label to display the background image
        self.background_label = tk.Label(self, image=self.background_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the entire window


        self.title_label = ttk.Label(self, text="LaLiga", font=("Arial", 16, "bold"))

        self.week_label = ttk.Label(self, text="Week:")
        self.team_label = ttk.Label(self, text="Team:")

        self.week_dropdown = ttk.Combobox(self, textvariable=self.week_var, values=list(range(1, 39)), state="readonly")
        self.team_dropdown = ttk.Combobox(self, textvariable=self.team_var, values=self.teams, state="readonly")

        self.select_all_checkbox = ttk.Checkbutton(self, text="Select all weeks", variable=self.select_all_var,
                                                   command=self.toggle_week_dropdown)

        self.results_text = tk.Text(self, height=10, width=50, state='disabled')

        self.show_button = ttk.Button(self, text="Show Matches", command=self.show_matches)

        self.create_layout()

    def create_layout(self):
        self.title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.week_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.week_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.select_all_checkbox.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.team_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.team_dropdown.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.show_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        self.results_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def show_matches(self):
        selected_team = self.team_var.get()

        # Replace 'LaLiga_matches.csv' with the path to your LaLiga CSV file
        with open('laliga-stats.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            results = []
            for row in csv_reader:
                week = int(row[0])
                home_team = row[2]
                away_team = row[4]

                if self.select_all_var.get() or week == int(self.week_var.get()):
                    if selected_team == home_team or selected_team == away_team:
                        week_info = f"Week {row[0]}\n"
                        date_info = f"Date: {row[1]}\n"
                        result_info = f"Result: {row[2]} {row[3]} {row[4]}\n"

                        results.append(week_info + date_info + result_info)

            self.results_text.config(state='normal')
            self.results_text.delete('1.0', tk.END)

            if results:
                self.results_text.insert(tk.END, '\n'.join(results))
            else:
                self.results_text.insert(tk.END, "No matches found.")

            self.results_text.config(state='disabled')

    def toggle_week_dropdown(self):
        if self.select_all_var.get():
            self.week_dropdown.config(state='disabled')
        else:
            self.week_dropdown.config(state='readonly')


if __name__ == '__main__':
    app = LaLigaResultsApp()
    app.mainloop()