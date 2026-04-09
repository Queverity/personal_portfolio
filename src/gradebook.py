# CB 1st Gradebook Class

from gradebook_student import *
from gradebook_helper import *
import csv

# class Gradebook():
    # def __init__(self, catalog = []):
        # catalog is just a list

    # search_student(self):
        # ask user if they would like to search by name or id
        # if name, have user enter name, then iterate through catalog to see which names match, and print those, along with more specific details
        # if id, have user enter id, then iterate through catalog to see which id matches, then print that out

    # edit_student(self):
        # iterate through catalog and print out
        # have user choose student
        # ask user if they would like to edit name, id, add a grade, or remove a grade
        # for name or id, just have user input something new
        # for grades, call methods built into student class

    # add_student(self):
        # have user enter student name and id
        # create student object and save to csv

    # remove_student(self):
        # go through catalog and print out student names and ids
        # ask user who they would like to remove
        # remove that student from catalog

    # view_all()

    # find_average(self):
        # go through catalog, and add each grade in each students list to one big list
        # sum that list and divide by length to find average

    # find_high_low(self):
        # use lambda function to sort catalog list
        # highest will be last index, lowest will be first index (sort based on average)

# def initialize_catalog(students):
    # iterate through students list after loading from CSV and add them one by one to the catalog
    # okay so actually since you can save lists to CSVs, just set it to that

grade_levels = ["9th","10th","11th","12th"]

class Gradebook():

    def __init__(self,catalog = []):
        # the only attribute needed here is catalog. Its default will be an empty list for when the file is empty.
        self.catalog = catalog
    
    def search_student(self,query,mode):
        # First, create a list to store the student objects in. Then, check the mode the function is being run in. If name, take query and see if it is anywhere in the student object name attribute that is being iterated over. If it is, add that object to the found_students list. If ID, once an id is found that is equal to the query, add that student to the found_students list, and break the for loop. Each ID is unique, so only one student can have a given ID. After the loop, return found students.
        found_students = []
        if mode == "name":
            for i in self.catalog:
                if query.title() in i.name.title():
                    found_students.append(i)
                else:
                    pass
        else:
            for i in self.catalog:
                if query.title() == i.id:
                    found_students.append(i)
                    break
                else:
                    pass
        
        return found_students

    def edit_student(self):
        # check if there are any students to edit
        if bool(self.catalog) == False:
            print("You have no students saved in your gradebook.")
            return
        
        # print all avaiable students
        while True:
            for i in self.catalog:
                print(f"Name: {i.name} | ID: {i.id}")

            # have user choose which student they want to edit 
            choice = input("Enter ID of student you want to edit:\n").strip()

            # variable used in case ID is not found
            found = False
            # iterate through gradebook catalog, looking for student which matches given ID
            for i in self.catalog:
                if choice == i.id.strip():
                    found = True
                    while True:
                        # give user options on how to edit student
                        print(f"How would you like to edit student {i.id}?\n1. Add Grade\n2. Remove Grade\n3. Change Name\n4. Change ID\n5. Return to Gradebook Menu")

                        # take user input
                        choice = input("Enter number:\n").strip()

                        clear_screen()

                        # compare user input to available options
                        match choice:
                            case "1":
                                # if add grade, call add grade method from student class
                                i.add_grade()
                                print("Grade succesfully added.")
                                continue
                            case '2':
                                # if remove grade, call remove grade method from student class
                                i.remove_grade()
                                continue
                            case '3':
                                while True:
                                    # have user enter new student name, and make sure it isn't just the same name
                                    new_name = input(f"What would you like to change student {i.id}'s name to?").strip()
                                    if new_name.lower() == i.name.lower():
                                        print("That is the same name.")
                                        continue
                                    else:
                                        # set object name attribute to given name
                                        i.name = new_name
                                        break
                                after_action()
                                continue
                            case '4':
                                while True:
                                    # have user enter new ID, and make sure it isn't the same ID
                                    new_id = input(f"What would you like to change {i.name}'s ID to?").strip()
                                    if new_id.lower() == i.id.lower():
                                        print("That is the same ID.")
                                        continue
                                    else:
                                        # set object id attribute to given id
                                        i.id = new_id
                                        break
                                after_action()
                                continue
                            case '5':
                                # head back to main menu
                                return
                            case _:
                                # stupid proofing
                                print("Please enter 1, 2, 3, 4, or 5.")

                else:
                    pass
            
            # if found is never set to true, meaning the user entered an id for a student that didn't exist
            if found == False:
                print("Please enter a valid ID.")
                continue
            else:
                pass

    # method for creating student
    def add_student(self):
        # have user enter student name, no checks on this
        student_name = input("Enter name for new student:\n").strip()
        while True:
            # have user enter student grade level, and make sure it is a valid grade
            student_level = input("Enter grade level (9th, 10th, 11th, 12th) for new student:\n").strip()
            if student_level not in grade_levels:
                print("Please enter a grade level of 9th, 10th, 11th, or 12th.")
                continue
            break

        while True:
            # have user enter student ID, and make sure that ID is already taken, and that they actually entered something
            student_id = input("Enter ID for new student:\n").strip()

            if bool(student_id) == False:
                print("Please actually enter an ID.")
                continue
            
            id_check = False

            for i in self.catalog:
                if student_id == i.id.strip():
                    print("There is already a student with that ID in the gradebook. Please enter a different ID.")
                    id_check = True
                    break
            
            if id_check == True:
                continue

            break

        # set all values that aren't already set
        academic_standing = "N/A"
        average = "N/A"
        grade1 = "N/A"
        grade2 = "N/A"
        grade3 = "N/A"
        grade4 = "N/A"
        grade5 = "N/A"
        grade6 = "N/A"
        grade7 = "N/A"
        grade8 = "N/A"

        # append new student object to gradebook catalog
        self.catalog.append(create_student(student_name,student_id,academic_standing,student_level,average,grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8))

        print("Student succesfully added!")

        after_action()
        return
    
    # method for removing students from gradebook
    def remove_student(self):
        # show avaiable students
        for i in self.catalog:
                print(f"Student Name: {i.name} | Student ID: {i.id}")
        while True:
            # have user enter student ID of student they want to remove
            delete_student = input("Enter ID of student you want to remove.").strip()

            for i in self.catalog:
                # if a match is found for entered id
                if i.id == delete_student:
                    # locate index of student object in list
                    student_index = find_object_index(self.catalog,delete_student)
                    if student_index == -1:
                        print("Student could not be found.")
                        after_action()
                        return
                    # remove student object using found index
                    self.catalog.pop(student_index)
                    print("Student succesfully removed.")
                    after_action()
                    return

    # for viewing students, use __str__ function already in student class and add a few things on
    def view_all(self):
        for i in self.catalog:
            print(i,f" | Grade Average: {i.average}% | Letter Grade: {i.calculate_letter()}")

        after_action()

    # method for finding overall class average
    def find_average(self):
        class_grades = []

        # go through students in catalog, add student averages to class grades list
        for i in self.catalog:   
            if i.average == "N/A":
                pass
            else:
                class_grades.append(float(i.average))

        # sum class_grades list, than divide sum by length to get average
        class_sum = sum(class_grades)
        class_average = (class_sum)/len(class_grades)

        return class_average
    
    # method for finding student with worst grade and student with best grade
    def find_high_low(self):
        class_grades = []

        # create list of class averages
        for i in self.catalog:   
            if i.average == "N/A":
                pass
            else:
                class_grades.append(float(i.average))

        # sort the class grades, lowest to highest
        class_grades.sort()

        # highest grade is at end of list, lowest is at start
        high_student = class_grades[-1]
        low_student = class_grades[0]

        return high_student,low_student
    
    # method for saving gradebook catalog
    def save_students(self):
        # use with open to make sure the file closes automatically
        with open("documents\gradebook.csv",mode="w",newline="") as students:
            fieldnames = ['name','id','academic_standing','grade_level','grade1','grade2','grade3','grade4','grade5','grade6','grade7','grade8','average']
            writer = csv.DictWriter(students,fieldnames)
            basic_writer = csv.writer(students)

            # make sure fieldnames are written
            basic_writer.writerow(fieldnames)
            
            # write each object to csv, make sure object is read as a dictionary
            for i in self.catalog:
                writer.writerow(vars(i))