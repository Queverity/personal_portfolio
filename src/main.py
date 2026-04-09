# CB 1st Personal Portfolio Main File

# import all neccesary functions to actually run the programs
from fractal_generator import *
from movie_reccomender import *
from gradebook_interface import *
from update_personal_library import *

# import subprocess and sys for running the programs from the GUI
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
    # create app and set basic details
    app = ctk.CTk()
    app.title("Clayton Baird - Personal Portfolio")
    app.geometry("1600x1200")

    # labels for explaining what the program is
    introduction_label = ctk.CTkLabel(app, text="Welcome to my personal portfolio! To view project details, click on that project's button. To run a selected program, click the 'Run Program' button.", bg_color="transparent", text_color="black", font=ctk.CTkFont(size=16))
    introduction_label.pack(pady=20)

    # variable used later when running the program, to determine which program to run based on which button was clicked. I used a list so that it would be mutable within the lambda function for the buttons.
    selected_project = [None]  # Use list to make it mutable in lambda

    # function for changing explanation label later so user can see descriptions of the programs before running them
    def edit_label(project):
        selected_project[0] = project
        if project == "fractal":
            explanation_label.configure(text="This is a Sierpinski Triangle Fractal Generator! It will generate a triangle based on the fractal depth, color, and background color you set. With this program, I learned how to use recursive functions to draw the fractal. A challenge I overcame was figuring out the logic for the fractal, as it was very confusing to me at first.")
        elif project == "movie":
            explanation_label.configure(text="This program is a movie reccomender! You can use it to search through a pre-made list of movies based on a variety of different filters, see the full movie list, or add something to the movie list! With this program, I learned how to read and write to a CSV file, as well as how to use the csv module in Python. A challenge I overcame was getting the saving and loading to work properly, as it was entirely new to me.")
        elif project == "gradebook":
            explanation_label.configure(text="This program is a gradebook interface! You can use it to view all students in the gradebook, add students, remove students, search for students, edit student information, view class statistics, and save the gradebook. With this program, I learned how to use classes and objects, and also learned how to manage class relationships. A challenge I overcame was figuring out how I would save the student objects, as it was confusing to me at first, since I didn't really understand classes at the time.")
        elif project == "library":
            explanation_label.configure(text="This program is a personal library updater! You can use it to view your current library list, add items to your library list, remove items from your library list, and save your library list. With this program, I learned even more so how to work with CSV files in python, as well as how to make a filtering function for a list. A challenge I overcame was figuring out how to filter the library list based on user input, as it was a bit tricky to get the logic right for that.")


    # function for running the selected program
    def run_program():
        print("Loading program...")
        project = selected_project[0]
        # python is put at the start so the program is ran in the vscode terminal, and the cwd is set to the src folder so that the programs can be ran without any issues with file paths
        if project == "fractal":
            subprocess.run(['python', 'src\\fractal_generator.py'], cwd='.')
        elif project == "movie":
            subprocess.run(['python', 'src\\movie_reccomender.py'], cwd='.')
        elif project == "gradebook":
            subprocess.run(['python', 'src\\gradebook_interface.py'], cwd='.')
        elif project == "library":
            subprocess.run(['python', 'src\\update_personal_library.py'], cwd='.')

    # buttons for seeing details of program
    fractal_button = ctk.CTkButton(app, text="Fractal Generator",fg_color="lightblue", hover_color="blue", text_color="black", font=ctk.CTkFont(size=14), command=lambda: edit_label("fractal"))

    movie_button = ctk.CTkButton(app, text="Movie Reccomender", fg_color="lightblue", hover_color="blue", text_color="black", font=ctk.CTkFont(size=14), command=lambda: edit_label("movie"))

    gradebook_button = ctk.CTkButton(app, text="Gradebook Interface", fg_color="lightblue", hover_color="blue", text_color="black", font=ctk.CTkFont(size=14), command=lambda: edit_label("gradebook"))

    library_button = ctk.CTkButton(app, text="Personal Library Updater", fg_color="lightblue", hover_color="blue", text_color="black", font=ctk.CTkFont(size=14), command=lambda: edit_label("library"))

    # label to see program descriptions
    explanation_label = ctk.CTkLabel(app, text="Program Details Go Here (click a button)", bg_color="transparent", text_color="black", font=ctk.CTkFont(size=16),wraplength=1000)

    # button to run program, just calls run_program function
    run_program_button = ctk.CTkButton(app, text="Run Selected Program (Note: Programs will run in terminal)", fg_color="green", hover_color="lightgreen", text_color="black", font=ctk.CTkFont(size=14), command=lambda: run_program())

    # pack all the buttons and labels, and set the size of the buttons
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