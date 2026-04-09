# CB 1st Saving Parsing Files

import csv
from gradebook_helper import *

# def load_students():
    # use with open to load the file so it will close on its own
    # for name, id, academic_standing, and grade_level, just read them normally
    # for grades, put them each into a list, and then add that to the dictionary (if a grade is N/A, that just means no grade has been entered)

# def save_students():
    # use with open to the load the file so it will close on its own
    # for name, id, academic_standing, and grade_level, just write them normally
    # iterate through grades list and write that

# def initialize_students():
    # to be used if user enters a file path that leads to a non-existent file
    # create the file with the proper fieldnames, found in students.csv

def load_students():
    # use with open to make sure the file closes on its own
    with open("documents\\gradebook.csv", mode="r") as students:
        fieldnames = ['name','id','academic_standing','grade_level','grade1','grade2','grade3','grade4','grade5','grade6','grade7','grade8','average']
        reader = csv.DictReader(students,fieldnames)
        # done so fieldnames is not read
        next(students)

        # create list for student dictionaries to be held in
        students = []

        # append each student dictionary to list
        for i in reader:
            students.append(i)

        # return students list
        return students