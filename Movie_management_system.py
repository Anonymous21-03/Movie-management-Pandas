import pandas as pd
import datetime

# Global variable for the DataFrame
movies = pd.DataFrame(columns=["movieId", "movieName", "dateOfBook", "timeOfBook"])

def save_movies():
    movies.to_csv('movies.csv', index=False)

def load_movies():
    global movies
    try:
        movies = pd.read_csv('movies.csv')
    except FileNotFoundError:
        movies = pd.DataFrame(columns=["movieId", "movieName", "dateOfBook", "timeOfBook"])

def addMovie():
    id = input("Enter the movie id: ")
    name = input("Enter the movie name: ")
    dateOfBook = datetime.date.today()
    timeOfBook = datetime.datetime.now().time()
    
    newMovie = pd.DataFrame({
        "movieId": [int(id)],
        "movieName": [name],
        "dateOfBook": [dateOfBook],
        "timeOfBook": [timeOfBook],
    })
    
    global movies
    movies = pd.concat([movies, newMovie], ignore_index=True)
    save_movies()  

def deleteMovie():
    global movies
    id=int(input("Enter ID: "))
    movies=movies.drop(movies[movies['movieId']==id].index)
    save_movies()

def searchMovie():
    global movies
    name=input("Enter the name of the movie: ")
    movie= movies[movies['movieName'].str.strip().str.lower() == name]

    print(movie)

def main():
    load_movies()  
    
    print("Pick a choice:\n1. Add a movie\n2. Delete Movie\n3. Search a movie")
    x = int(input("Enter the choice : "))
    
    if x == 1:
        addMovie()
    if x==2:
        deleteMovie()
    if x==3:
        searchMovie()
    else:
        print("wrong input")
    
    print("\nMovies DataFrame:")
    # print(movies)

if __name__ == "__main__":
    main()
