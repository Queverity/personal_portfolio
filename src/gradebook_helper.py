# function clear_screen():
    # print function to clear the screen, take this from another project

# function continue_screen():
    # print something like "Press Enter to Continue", put an input() statement after that

# function after_action():
    # combine clear_screen and continue_screen

# print character to to clear screen
def clear_screen():
    print("\033c", end="")

# print a continue message, don't move on until user presses enter
def continue_screen():
    print("Press Enter to continue.")
    input()

# combine continue and clear
def after_action():
    continue_screen()
    clear_screen()

# used when removing students from gradebook
def find_object_index(list_of_objects,value):
    # iterate through gradebook
    for i in list_of_objects:
        # check if id is equal to given id
        if i.id.strip() == value.strip():
            # return the index of the object in the list
            return list_of_objects.index(i)
    
    # if nothing is found, return -1
    return -1