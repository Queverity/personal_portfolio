# CB 1st Updated Personal Library

import csv

# function to turn the library data into something we can use
def library_parser():
    # opening the file
    with open("documents//personal_library.csv",mode="r") as library:
        # turn each row in the file into a dictionary
        reader = csv.DictReader(library)
        # list to put each dictionary in
        items = []
        # iterate through reader, append each dict to items
        for line in reader:
            items.append(line)
        return items

# function to see if something actually exists in the library
def check_if_exists(library,new_thing,mode):
    # iterate through the movies list to see if the given title is already in the movie list

    # see if there is anything in the library list, if not, return
    if bool(library) == False:
        return
    else:
        # check to see which mode the function is being used in
        if mode == "1":
            # when trying to add an item, iterate through the list to see if that title is already in the library. If it is, return false
            for media in library:
                if new_thing.lower() == media['title'].lower():
                    print("That media is already in the list.")
                    return False
            return True
        
        elif mode == "2":
            # when trying to delete or update an item, make sure the item actually exists in the list.
            for media in library:
                if new_thing.lower() == media['title'].lower():
                    return True
            return False

# function for a simple view of the library
def basic_view(library):
    # checking to see if there is anything in the library
    if bool(library) == False:
        print("Your library is empty.")
        return
    else:
        # iterate through the items in the library, print their title and creator
        for i in library:
            number = library.index(i) + 1
            print(f"{number}. {i['title']} by {i['creator']}")

# function for a more detailed view of the library
def detailed_view(library):
    # checking to see if there is anything in the library
    if bool(library) == False:
        print("Your library is empty.")
        return
    # itereate through the items in the library, print all the information about them
    else:
        for i in library:
            number = library.index(i) + 1
            print(f"{number}. {i['title']} by {i['creator']}. A(n) {i['genre']} (whatever it is) published in {i['year']}.")

# function for adding items to the library
def add_item(library):
    # new dictionary item for whatever is being added
    new_media = {}
    while True:
        # take in new title, run the check_if_exists function to see if it is already in the library
        new_title = input("Enter the title of the media you are adding:\n").strip()
        title_check = check_if_exists(library,new_title,mode="1")
        if title_check == False:
            continue
        else:
            # get all the other information for the item being added
            new_creator = input("Enter the name of the creator of the media you are adding:\n").strip()
            new_year = input("Enter the year of release for the media you are adding:\n").strip()
            new_genre = input("Enter the genre of the media you are adding:\n").strip()
            break
    
    # add all the information to the new item, return it
    new_media['title'] = new_title
    new_media['creator'] = new_creator
    new_media['year'] = new_year
    new_media['genre'] = new_genre

    return new_media

# function for removing items from the library
def delete_item(library):
    # check if the library is empty
    if bool(library) == False:
        print("Your library is empty.")
        return
    else:
        # show what exists in the library
        basic_view(library)
        while True:
            # take in name of what user wants to remove, check if it actually exists in the library
            item_to_delete = input("Enter the name of the media you want to remove exactly as seen in the list.").lower().strip()
            exists = check_if_exists(library,item_to_delete,mode="2")
            if exists == False:
                print("That is not an item in the library.")
            else:
                # iterate through the library, if the title of the item matches the title entered, remove that item
                for i in library:
                    if item_to_delete == i['title'].lower():
                        library.remove(i)
                        break
                    else:
                        pass
                break
        # return new library
        return library
 
# function for updating an item in the library
def update_item(library,new_thing,item_to_update,mode):
    # iterate through the library
    for item in library:
        # look for the item that the user wants to update
        if item_to_update == item['title'].lower():
            # set the thing the user wanted to update about the item to the new value, return the item
            item[mode] = new_thing
            return item

# UI for updating an item
def update_item_menu(library):
    # check if the library is empty
    if bool(library) == False:
        print("Your library is empty.")
        return
    else:
        # give detailed view of items in teh library
        detailed_view(library)
        while True:
            # get title of item user wanted to update, see if it actually exists
            item_to_update = input("Enter the name of the media you want to update exactly as seen on the list.").lower()
            exists = check_if_exists(library,item_to_update,mode="2")
            if exists == False:
                print("That piece of media is not in the list.")
                continue
            else:
                while True:
                    # see what user wants to update about the item
                    thing_to_change = input("What would you like to update?\n1. Title\n2. Creator Name\n3. year of Release\n4. Genre(s)\nEnter number:\n").strip()
                    match thing_to_change:
                        # check what user entered
                        case "1":
                            # take in new value, run that through the update_item function, then set the item in the list to the new item. After that, return library. This works the same for all the other cases. Note: I know this is garbage and could probably be better done with more functions, but I couldn't figure out how to make that work.
                            new_title = input("Enter the new title for the media you are updating.").strip()
                            updated_item = update_item(library,new_title,item_to_update,mode='title')
                            for item in library:
                                if item_to_update == item['title'].lower():
                                    item = updated_item
                            return library
                        case "2":
                            new_creator = input("Enter the name of the creator for the media you are updating.").strip()
                            updated_item = update_item(library,new_creator,item_to_update,mode='creator')
                            for item in library:
                                if item_to_update == item['title'].lower():
                                    item = updated_item
                            return library
                        case "3":
                            new_year = input("Enter the year of release for the media you are updating.").strip()
                            updated_item = update_item(library,new_year,item_to_update,mode='year')
                            for item in library:
                                if item_to_update == item['title'].lower():
                                    item = updated_item
                            return library
                        case "4":
                            new_genres = input("Enter the new genre(s) for the media you are updating. If there are multiple, seperate them with a forward slash (/).").strip()
                            updated_item = update_item(library,new_genres,item_to_update,mode='genre')
                            for item in library:
                                if item_to_update == item['title'].lower():
                                    item = updated_item
                            return library
                        case _:
                            # stupid proofing
                            print("Please enter 1, 2, 3, or 4.")
                            continue

# function for searching for an item
def search_for_item(matching_items,mode,library,query):
    matching_items = []
    # iterate through the library, check if the specific thing we're interesteed in about the item matches the search term, if it does, add it to the matching items list
    for i in library:
        if query.lower() in i[mode].lower():
            matching_items.append(i)

    return matching_items

# UI for searching for an item
def search_library(library):
    # check to see if the library is empty
    if bool(library) == False:
        print("Your library is empty.")
        return
    else:
        matching_items = library
        while True:
            # ask what user would like to search by
            search_item = input("What would you like to search by?\n1. Title\n2. Creator Name\n3. Year of Release\n4. Genre(s)\nEnter number:\n").strip()
            match search_item:
                # set mode equal to what the user asked for, ask them for the search term, then run it through the search_for_item function. This works the same for the other cases.
                case "1":
                    mode = 'title'
                    search_term = input("Enter the title of the item you want to find:\n").lower()
                    matching_items = search_for_item(matching_items,mode,library,search_term)
                case "2":
                    mode = 'creator'
                    search_term = input("Enter the name of the creator of the item you want to find:\n").lower()
                    matching_items = search_for_item(matching_items,mode,library,search_term)
                case "3":
                    mode = 'year'
                    search_term = input("Enter the release year of the item you want to find:\n").lower()
                    matching_items = search_for_item(matching_items,mode,library,search_term)
                case "4":
                    mode = 'genre'
                    search_term = input("Enter the genre of the item you want to find:\n").lower()
                    matching_items = search_for_item(matching_items,mode,library,search_term)
                case _:
                    # stupid proofing
                    print("Please enter 1, 2, 3, or 4.")
                    continue
            # check if user would like to refine their search
            continue_searching = input("Would you like to continue refining your search? Y/N:\n").strip().capitalize()
            if continue_searching == "Y":
                continue
            else:
                return matching_items

# function for saving the library
def save_library(library):

    # This clears the library file.
    with open("documents//personal_library.csv",mode="w") as new_library:
        writer = csv.writer(new_library)
        writer.writerow(['title','creator','year','genre'])

    # Iterate through the library list, appending each dictionary (book) to the csv file on a new row
    with open("documents//personal_library.csv",mode="a",newline='') as new_library:
        fieldnames = ['title','creator','year','genre']
        writer = csv.DictWriter(new_library,fieldnames)
        for i in library:
            writer.writerow(i)

# main menu function
def library_menu():
    # get library list
    library = library_parser()
    # description of program
    print("This is a library manager. It saves to a file, so it actually persists across runs this time! You can view and search through your library, add items, delete items, and update items using this program.")
    # main loop
    while True:
        # check what user would like to do
        action = input("What would you like to do?\n1. Basic View\n2. Detailed View\n3. Add Item\n4. Delete Item\n5. Update Item\n6. Save Library\n7. Search through library\n8. Exit\nEnter number:\n").strip()
        match action:
            case "1":
                basic_view(library)
            case "2":
                detailed_view(library)
            case "3":
                # add the new_media to the library list after getting it from the add_item function
                new_media = add_item(library)
                library.append(new_media)
            case "4":
                library = delete_item(library)
            case "5":
                library = update_item_menu(library)
            case "6":
                # reset the library list variable to be equal to the new library file just to make sure
                save_library(library)
                library = library_parser()
                print("Library saved")
            case "7":
                # after getting the matching items list, iterate through it and print out a detailed view of all the items in it
                matching_items = search_library(library)
                print("Titles found:")
                if bool(matching_items) == False:
                    print("No items were found within those search terms.")
                else:
                    detailed_view(matching_items)
            case "8":
                # make sure user has saved
                check_if_save = input("Are you sure you want to exit? Any unsaved information will be lost. Y/N:\n").strip().capitalize()
                if check_if_save == "Y":
                    print("Goodbye!")
                    break
                else:
                    continue
            case _:
                # stupid proofing
                print("Please enter 1, 2, 3, 4, 5, 6, 7, or 8.")
                continue