#Pengkai Fang & Juntong Liu & Liming Zheng


movie = {}
class actor:
    def __init__(self, info):
        self.name = info[0]
        self.birth = info[1]
        self.nationality = info[2]

class properity:
    def __init__(self, Movie, Year, info, Genre, Review, Status, Counter):
        self.movie = Movie
        self.year = Year
        self.genre = Genre
        self.review = Review
        self.sta = Status
        self.actor = actor(info)
        self.count = Counter

def main_window():
    print("\n\n")
    print("choose option you want:\n")
    print("1. Add the movie properity")
    print("2. Choose the movie you want to watch.")
    print("3. Writing a review about a movie")
    print("4. Borrowing the movie")
    print("5. Returning the movie")
    print("6. list the detail of the movie")

def checkmovie_properity(properity):
    print("Movie:   " + properity.movie)
    print("Year:   " + str(properity.year))
    print("Genre:   " + properity.genre)
    print("actors' name:   " + properity.actor.name)
    print("actors' birth:" + properity.actor.birth)
    print("actors' nationality" + properity.actor.nationality)
    print("Review:   " + properity.review)
    print("Watch count:   " + str(properity.count))

while 1:
    main_window()
    option = int(input("Select your choice\n"))
    if option == 1:
        Movie = input("enter the movie name: ")
        Year = input("enter the movie year: ")
        Genre = input("enter movie genre: ")
        # info = actor.INFO
        AA = input("enter movie actors: ")
        BB = input("enter movie actors birth: ")
        CC = input("country:")
        XX = [AA,BB,CC]
        actor1 = actor(XX)

        Review = " "
        Status = True
        Counter = 0
        if Movie not in movie.keys():
            e = properity(Movie, Year, XX, Genre, Review, Status, Counter)
            movie[Movie] = e
            print(Movie + "  added\n")
        else:
            print(Movie + "  already in\n")

    elif option == 2:
        Movie = input("please input the name of movie you want to watch")
        Counter += 1
        e = properity(Movie, Year, XX, Genre, Review, Status, Counter)
        movie[Movie] = e

    elif option == 3:
        Movie = input("enter the movie name")
        Review = input("enter movie review")
        e = properity(Movie, Year, XX, Genre, Review, Status, Counter)
        movie[Movie] = e
        print(Movie + "  updated\n")

    elif option == 4:
        Movie = input("enter the movie name")
        if Status == True:

            Status = False
            e = properity(Movie, Year, XX, Genre, Review, Status, Counter)
            movie[Movie] = e
            print(Movie + "  borrowed\n")
        else:
            print(Movie + "  Not available right now" )


    elif option == 5:
        Movie = input("enter the movie name")
        Status = True
        e = properity(Movie, Year, XX, Genre, Review, Status, Counter)
        print(Movie + "   returned")

    elif option == 6:
        Movie = input("enter the movie name")
        checkmovie_properity(movie[Movie])
