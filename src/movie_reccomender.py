# CB 1st Movie Recommender

import csv

def list_parser():
    # using try/except for error handling
    try:
        # Open the movie list file, find the headers of the file, make a list of dictionaries where each dictionary is a movie
        with open("documents//movies_list.csv", mode = "r") as movies_list:
            content = csv.reader(movies_list)
            headers = next(content)
            movies = []
            for movie in content:
                movies.append({headers[0]: movie[0], headers[1]:movie[1], headers[2]:movie[2], headers[3]:movie[3], headers[4]:movie[4], headers[5]:movie[5],})
    # if the CSV cannot be opened for some reason
    except:
        print("Couldn't open the CSV")
    # when the CSV is opened succesfully
    else:
        return movies

def movie_filters(movies):
    # set the matching movies variable equal to the movies list
    matching_movies = movies

    def title_filter(movies = matching_movies):
        matching_movies = []
        # use .lower() to make everything case-insensitive
        query = input("Enter the title of the movie you want to search for:\n").lower()
        # iterate through the movies list, see if the given title is in any of the titles in the movie list, if so, add that movie to matching movies
        for movie in movies:
            if query.lower() in movie['Title'].lower():
                matching_movies.append(movie)
        return matching_movies
    
    def director_filter(movies = matching_movies):
        matching_movies = []
        # same logic as the title filter
        query = input("Enter the director of the movie you want to search for:\n").lower()
        for movie in movies:
            if query in movie['Director'].lower():
                matching_movies.append(movie)
        return matching_movies
    
    def genre_filter(movies = matching_movies):
        matching_movies = []
        # same logic as the title filter
        query = input("Enter the genre of the movie you want to search for:\n").lower()
        for movie in movies:
            if query in movie['Genre'].lower():
                matching_movies.append(movie)
        return matching_movies
    
    def rating_filter(movies = matching_movies):
        matching_movies = []
        # same logic as the title filter
        query = input("Enter the rating (G, PG, PG-13, R) of the movie you want to search for:\n").lower()
        for movie in movies:
            if query == movie['Rating'].lower():
                matching_movies.append(movie)
        return matching_movies
    
    def length_filter(movies = matching_movies):
        matching_movies = []
        while True:
            # use try/accept to make sure user actually enters a number
            query = input("Enter the length (in min) of the movies you want to search for. Any movies that are shorter or equal to this length will be found. Enter number:\n")
            try:
                query = int(query)
            except:
                print("Please enter a number.")
                continue

            for movie in movies:
                # see if the movie length is less than or equal to the given length
                if query >= movie['Length (min)'].lower():
                    matching_movies.append(movie)
            return matching_movies
    
    def actors_filter(movies = matching_movies):
        matching_movies = []
        # same logic as the title filter
        query = input("Enter the notable actors of the movie you want to search for:\n").lower()
        for movie in movies:
            if query in movie['Notable Actors'].lower():
                matching_movies.append(movie)
        return matching_movies
    
    while True:
        # ask which filter the user wants to use, after that, check if they want to continue filtering. The next filters will use the matching_movies list returned by the first filter.
        filter_type = input("How would you like to filter your movies?\n1. By Title\n2. By Director(s)\n3. By Rating\n4. By Length\n5. By Notable Actors\n6. By Genre\nEnter Number:\n").strip()
        match filter_type:
            case "1":
                matching_movies = title_filter(movies = matching_movies)
            case "2":
                matching_movies = director_filter(movies = matching_movies)
            case "3":
                matching_movies = rating_filter(movies = matching_movies)
            case "4":
                matching_movies = length_filter(movies = matching_movies)
            case "5":
                matching_movies = actors_filter(movies = matching_movies)
            case "6":
                matching_movies = genre_filter(movies = matching_movies) 
            case _:
                print("Please enter 1, 2, 3, 4, 5, or 6.")
                continue
        
        continue_filtering = input("Would you like to filter your movies more? Y/N:\n").strip().capitalize()
        if continue_filtering == "Y":
            continue
        else:
            return matching_movies

def check_title(movies,new_title):
    # iterate through the movies list to see if the given title is already in the movie list
    for title in movies:
        if new_title.lower() == title['Title'].lower():
            print("That movie is already in the list.")
            return False
    return True

def new_movie_data(movies):
    new_movie = []
    while True:
        new_title = input("Enter the title of the movie you want to add.").strip()
        title_check = check_title(movies,new_title)
        if title_check == False:
            continue
        else:
            new_directors = input("Enter the director(s) of the movie you want to add. Seperate director names with a comma").strip()
            new_genres = input("Enter the genre(s) of the movie you want to add. Seperate genres with a comma.").strip()
            new_rating = input("Enter the rating of the movie you want to add.").strip().upper()
            while True:
                new_length = input("Enter the length (in min) of the movie you want to add.").strip()
                try:
                    new_length = int(new_length)
                except:
                    print("Please enter a number.")
                    continue
                else:
                    break
            new_actors = input("Enter the notable actor(s) of the movie you want to add. Seperate actor names with a comma.").strip()

            new_movie.append(new_title)
            new_movie.append(new_directors)
            new_movie.append(new_genres)
            new_movie.append(new_rating)
            new_movie.append(new_length)
            new_movie.append(new_actors)
            return new_movie

def add_movie(new_movie):
    # open the movies list file, write the new_movie list to it
    try:
        with open("documents\\movies_list.csv",'a',newline='') as movies:
            writer = csv.writer(movies)
            writer.writerow(new_movie)
    except:
        print("The movie could not be written to the CSV file.")

def print_movies(movies):
    for line in movies:
        print(f"Title: {line['Title']} | Director(s): {line['Director']} | Genre(s): {line['Genre']} | Rating: {line['Rating']} | Length: {line['Length (min)']} | Notable Actors: {line['Notable Actors']}")              
            
def movie_main():
    # get the list of movies for use later in the program
    movies = list_parser()
    # basic explanation of the program
    print("This program is a movie reccomender! You can use it to search through a pre-made list of movies bsaed on a variety of different filters, see the full movie list, or add something to the movie list!")
    while True:
        # get input from user, use match/case to decide what to do with that input
        action = input("What would you like to do?\n1. Print Full Movie List\n2. Search/Get Reccomendations\n3. Add Movie\n4. Exit\nEnter Number:\n").strip()
        match action:
            case "1":
                # call the print_movies function to print the entire list
                print("Movie List:")
                print_movies(movies)
            case "2":
                matching_movies = movie_filters(movies)
                # see if the matching_movies list is empty
                if bool(matching_movies) == False:
                    print("No movies were found within those filters. Perhaps try removing or easing up on some filters.")
                else:
                    print_movies(matching_movies)
            case "3":
                # call the functions for adding a movie
                new_movie = new_movie_data(movies)
                add_movie(new_movie)
                # update the movies variable with the new movie
                movies = list_parser()
                pass
            case "4":
                # end the main loop
                print("Goodbye!")
                break
            # if user enters an invalid answer
            case _:
                print("Please enter 1, 2, 3, or 4.")
                continue

if __name__ == "__main__":
    movie_main()