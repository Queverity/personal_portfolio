# CB 1st Student Class

from gradebook_helper import *

# class Student:
    # def __init__(self):
        # attributes will be name, student_id, a grades list, academic standing, and grade level. grades_list will have a defualt value of an list with eight entries of 'N/A'

    # def __str__(self):
        # print student name, id, grade average, letter grade, academic standing, and grade level

    # def view_grades(self):
        # iterate through grades list and print items if not equal to 'N/A'
    
    # def calculate_average(self):
        # find both number and letter grade average (maybe also GPA)
        # go through student grades list, add up all items, divide by list length
        # take average and turn it into a letter grade

    # def find_standing(self):
        # take grade average, make a few if statements to find different things


    # def add_grade(self):
        # have user input grade
        # make sure grade is not above 100 or below 0
        # add grade to grades list and recalculate average and standing

    # def remove_grade(self):
        # go through grades list and print out each grade
        # have user input which grade they want to remove
        # if index does not exist, have user try again
        # if index does exist, pop grade from list and recalculate average and standing

# def create_student(name,id,grades):
    # create a student object using name and id, and grades if it is not empty
    # if bool(grades) != False:
        # student_object = Student(name,id,grades)
    # else:
        # student_object = Student(name,id)

class Student:
    # attributes important for student, along with each grade slot
    def __init__(self,name,id,academic_standing,grade_level,average):
        self.name = name
        self.id = id
        self.academic_standing = academic_standing
        self.grade_level = grade_level
        self.average = average
        self.grade1 = "N/A"
        self.grade2 = "N/A"
        self.grade3 = "N/A"
        self.grade4 = "N/A"
        self.grade5 = "N/A"
        self.grade6 = "N/A"
        self.grade7 = "N/A"
        self.grade8 = "N/A"

    def __str__(self):
        # print out important information of student
        return f"Student Name: {self.name} | Student ID: {self.id} | Academic Standing: {self.academic_standing} | Grade Level: {self.grade_level}"

    def grade_check(self):
        # see if all grade slots are taken, or if all grade slots are empty
        if self.grade1 != "N/A" and self.grade2 != "N/A" and self.grade3 != "N/A" and self.grade4 != "N/A" and self.grade5 != "N/A" and self.grade6 != "N/A" and self.grade7 != "N/A" and self.grade8 != "N/A":
            return "Full"
        elif self.grade1 == "N/A" and self.grade2 == "N/A" and self.grade3 == "N/A" and self.grade4 == "N/A" and self.grade5 == "N/A" and self.grade6 == "N/A" and self.grade7 == "N/A" and self.grade8 == "N/A":
            return "Empty"
        else:
            return

    def view_grades(self):
        # print out each grade slot
        return f"Grade One: {self.grade1}\nGrade Two: {self.grade2}\nGrade Three: {self.grade3}\nGrade Four: {self.grade4}\nGrade Five: {self.grade5}\nGrade Six: {self.grade6}\nGrade Seven: {self.grade7}\nGrade Eight: {self.grade8}\n"
        

    def calculate_average(self):
        # for each grade that actually has a number in it, increase length by one
        grades_length = 0
        if self.grade1 != "N/A":
            grades_length += 1
        if self.grade2 != "N/A":
            grades_length += 1
        if self.grade3 != "N/A":
            grades_length += 1
        if self.grade4 != "N/A":
            grades_length += 1
        if self.grade5 != "N/A":
            grades_length += 1
        if self.grade6 != "N/A":
            grades_length += 1
        if self.grade7 != "N/A":
            grades_length += 1
        if self.grade8 != "N/A":
            grades_length += 1

        # for each grade slot that actually has a number in it, add it to total
        grades_summed = 0
        if self.grade1 != "N/A":
            grades_summed += float(self.grade1)
        if self.grade2 != "N/A":
            grades_summed += float(self.grade2)
        if self.grade3 != "N/A":
            grades_summed += float(self.grade3)
        if self.grade4 != "N/A":
            grades_summed += float(self.grade4)
        if self.grade5 != "N/A":
            grades_summed += float(self.grade5)
        if self.grade6 != "N/A":
            grades_summed += float(self.grade6)
        if self.grade7 != "N/A":
            grades_summed += float(self.grade7)
        if self.grade8 != "N/A":
            grades_summed += float(self.grade8)
        

        # find average by dividing sum by length, then round
        grade_average = float(grades_summed / grades_length)
        grade_average = round(grade_average,2)

        return grade_average
    
    def calculate_letter(self):
        # if there is no average
        if self.average == "N/A":
            return "N/A"

        # bunch of if statements to check grade compared to limits
        if float(self.average) >= 94:
            return "A"
        elif float(self.average) >= 90:
            return "A-"
        elif float(self.average) >= 87:
            return "B+"
        elif float(self.average) >= 84:
            return "B"
        elif float(self.average) >= 80:
            return "B-"
        elif float(self.average) >= 77:
            return "C+"
        elif float(self.average) >= 74:
            return "C"
        elif float(self.average) >= 70:
            return "C-"
        elif float(self.average) >= 67:
            return "D+"
        elif float(self.average) >= 64:
            return "D"
        elif float(self.average) >= 61:
            return "D-"
        else:
            return "F"

    def find_standing(self,grade_average):
        # few if statements to compare grade average to preset standing limits
        if grade_average >= 90:
            return "Honor Roll"
        elif grade_average >= 80:   
            return "Good Standing"
        else:
            return "Needs Improvement"
        
    def add_grade(self):
        # see if all grade slots are taken; if so, tell user as much, then return
        check = self.grade_check()
        if check == 'Full':
            print("You have added the maximum number (8) of grades to this student. If you want to change a grade, first remove one.")
            return
        
        while True:
            # have user enter grade they want to add, or exit
            new_grade = input("Enter grade you want to add, or type 'exit' to return to gradebook menu:\n").strip().lower()

            if new_grade == 'exit':
                return
            else:
                try:
                    # make sure grade is actually a number
                    new_grade = float(new_grade)
                except:
                    print("Please enter an actual number.")
                    after_action()
                    continue
                else:
                    if new_grade > 100 or new_grade < 0:
                        # make sure grade is within limits
                        print("Please enter a number between 100 and 0.")
                        continue
                    else:
                        # go through grade slots and change the first empty one to new grade
                        if self.grade1 == "N/A":
                            self.grade1 = new_grade

                        elif self.grade2 == "N/A":
                            self.grade2 = new_grade

                        elif self.grade3 == "N/A":
                            self.grade3 = new_grade

                        elif self.grade4 == "N/A":
                            self.grade4 = new_grade

                        elif self.grade5 == "N/A":
                            self.grade5 = new_grade

                        elif self.grade6 == "N/A":
                            self.grade6 = new_grade

                        elif self.grade7 == "N/A":
                            self.grade7 = new_grade

                        elif self.grade8 == "N/A":
                            self.grade8 = new_grade

                        self.average = self.calculate_average()
                        self.academic_standing = self.find_standing(self.average)

                        return
                        
    def remove_grade(self):
        # list of valid inputs user can enter in later on input
        valid_inputs = ['1','2','3','4','5','6','7','8']

        check = self.grade_check()
        # see if there are already no grades in student
        if check == 'Empty':
            print("You have no grades entered for this student.")
            return
        while True:
            # print out all grades
            print(f"1. {self.grade1}\n2. {self.grade2}\n3. {self.grade3}\n4. {self.grade4}\n5. {self.grade5}\n6. {self.grade6}\n7. {self.grade7}\n8. {self.grade8}")

            # ask user which grade they want to remove
            grade = input("Enter the number by the grade you want to remove. If the grade is shown as N/A, no grade has been entered for that slot.:\n").strip()

            if grade not in valid_inputs:
                # if user has entered a number not 1 - 8
                print("Please enter a number 1 - 8.")
            else:
                match grade:
                    # check which grade user entered, set it to N/A
                    case '1':
                        self.grade1 = "N/A"
                    case '2':
                        self.grade2 = "N/A"
                    case '3':
                        self.grade3 = "N/A"
                    case '4':
                        self.grade4 = "N/A"
                    case '5':
                        self.grade5 = "N/A"
                    case '6':
                        self.grade6 = "N/A"
                    case '7':
                        self.grade7 = "N/A"
                    case '8':
                        self.grade8 = "N/A"

                print("Grade succesfully removed.")
                return
                
    

                
# function to quickly create student object, set all grades to input grades
def create_student(name,id,academic_standing,grade_level,average,grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8):
    student_object  = Student(name,id,academic_standing,grade_level,average)
    student_object.grade1 = grade1
    student_object.grade2 = grade2
    student_object.grade3 = grade3
    student_object.grade4 = grade4
    student_object.grade5 = grade5
    student_object.grade6 = grade6
    student_object.grade7 = grade7
    student_object.grade8 = grade8

    return student_object