#Create a program to create a movie class.Add relevant attributes and functions with it.
class Movie:
    def __init__(self, title, director, year, genre, rating):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.rating = rating

    def display_info(self):
        print(" Movie Details ")
        print("Title     : {self.title}")
        print("Director  : {self.director}")
        print("Year      : {self.year}")
        print("Genre     : {self.genre}")
        print("Rating    : {self.rating}/10")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print("Rating updated to {self.rating}/10")


# Main Program (User Input)
print("Enter Movie Details:")
title = input("Enter movie title: ")
director = input("Enter director name: ")
year = int(input("Enter release year: "))
genre = input("Enter genre: ")
rating = float(input("Enter rating (out of 10): "))

# Create movie object
movie1 = Movie(title, director, year, genre, rating)

# Display movie details
movie1.display_info()

# Update rating
new_rating = float(input("Enter new rating to update: "))
movie1.update_rating(new_rating)

# Display updated details
movie1.display_info()
class Movie:
    def __init__(self, title, director, year, genre, rating):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.rating = rating

    def display_info(self):
        print("Movie Details")
        print("Title     : {self.title}")
        print("Director  : {self.director}")
        print("Year      : {self.year}")
        print("Genre     : {self.genre}")
        print("Rating    : {self.rating}/10")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print("Rating updated to {self.rating}/10")


# Main Program (User Input)
print("Enter Movie Details:")
title = input("Enter movie title: ")
director = input("Enter director name: ")
year = int(input("Enter release year: "))
genre = input("Enter genre: ")
rating = float(input("Enter rating (out of 10): "))

# Create movie object
movie1 = Movie(title, director, year, genre, rating)

# Display movie details
movie1.display_info()

# Update rating
new_rating = float(input("\nEnter new rating to update: "))
movie1.update_rating(new_rating)

# Display updated details
movie1.display_info()
