# CB 1st Personal Portfolio Main File

from fractal_generator import *
from movie_reccomender import *
from gradebook_interface import *
from update_personal_library import *

import subprocess
import sys
import customtkinter as ctk

# define function init_window():
    # create a customtkinter window
    # set title to Clayton Baird - Personal Portfolio
    # set size to 800x600
    # set background color to white
    # make four buttons for each project (these will put project details into a different label when clicked)
    # create button to run the selected program

def init_window():
    app = ctk.CTk()
    app.title("Clayton Baird - Personal Portfolio")
    app.geometry("1600x1200")
    app.configure(bg="white")

    explanation_label = ctk.CTkLabel(app, text="Welcome to my personal portfolio! Please select a project to view details and run the program.", bg_color="white", text_color="black", font=ctk.CTkFont(size=16))
    explanation_label.pack(pady=20)

    def edit_label(project):
        if project == "fractal":
            explanation_label.configure(text="This is a Sierpinski Triangle Fractal Generator! It will generate a triangle based on the fractal depth, color, and background color you set.")
        elif project == "movie":
            explanation_label.configure(text="This program is a movie reccomender! You can use it to search through a pre-made list of movies based on a variety of different filters, see the full movie list, or add something to the movie list!")
        elif project == "gradebook":
            explanation_label.configure(text="This program is a gradebook interface! You can use it to view all students in the gradebook, add students, remove students, search for students, edit student information, view class statistics, and save the gradebook.")
        elif project == "library":
            explanation_label.configure(text="This program is a personal library updater! You can use it to view your current library list, add items to your library list, remove items from your library list, and save your library list.")

    def run_program(project):
        if project == "fractal":
            subprocess.run([sys.executable, "fractal_generator.py"])
        elif project == "movie":
            subprocess.run([sys.executable, "movie_reccomender.py"])
        elif project == "gradebook":
            subprocess.run([sys.executable, "gradebook_interface.py"])
        elif project == "library":
            subprocess.run([sys.executable, "update_personal_library.py"])

    fractal_button = ctk.CTkButton(app, text="Fractal Generator",fg_color="lightblue", hover_color="blue", text_color="black", font=ctk.CTkFont(size=14), command=lambda: edit_label("fractal"))

    movie_button = ctk.CTkButton(app, text="Movie Reccomender", fg_color="lightblue", hover_color="blue", text_color="black", font=ctk.CTkFont(size=14), command=lambda: edit_label("movie"))

    gradebook_button = ctk.CTkButton(app, text="Gradebook Interface", fg_color="lightblue", hover_color="blue", text_color="black", font=ctk.CTkFont(size=14), command=lambda: edit_label("gradebook"))

    library_button = ctk.CTkButton(app, text="Personal Library Updater", fg_color="lightblue", hover_color="blue", text_color="black", font=ctk.CTkFont(size=14), command=lambda: edit_label("library"))

    explanation_label = ctk.CTkLabel(app, text="Program Details Go Here (click a button)", bg_color="white", text_color="black", font=ctk.CTkFont(size=16))

    run_program_button = ctk.CTkButton(app, text="Run Program (Note: Programs will run in terminal)", fg_color="green", hover_color="lightgreen", text_color="black", font=ctk.CTkFont(size=14), command=lambda: run_program(explanation_label.cget("text")))

    fractal_button.pack(pady=50)
    movie_button.pack(pady=50)
    gradebook_button.pack(pady=50)
    library_button.pack(pady=50)
    explanation_label.pack(pady=70)
    run_program_button.pack(pady=50)

    fractal_button.configure(width=200, height=50)
    movie_button.configure(width=200, height=50)
    gradebook_button.configure(width=200, height=50)
    library_button.configure(width=200, height=50)
    run_program_button.configure(width=300, height=50)
    app.mainloop()

init_window()