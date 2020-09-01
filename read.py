#reading txt file.
def read_movie():
    file = open("movies.txt", "r")
    content = file.readlines()
    list_movie = []
    dictionary_movie = {}
    for i in content:
        list_movie.append(i.replace("\n","").split(","))

    for i in range(len(list_movie)):
        key = list_movie[i][0]
        value = []
        for j in range(1,len(list_movie[0])):
            value.append(list_movie[i][j])
            dictionary_movie[key] = value
    return dictionary_movie


dictionary_movie = read_movie()
#function return the movies id from dictionary_movies
def movieid():
    movie_id = []
    for key in dictionary_movie.keys():
        movie_id.append(key)
    return movie_id
movie_id = movieid()

#display function to display the movie in program
def display():
    print("MovieId \t\t MovieName \t\t\tPrice \t\t\t Quantity")
    for key,value in dictionary_movie.items():
        print(key+"\t\t\t"+value[0]+"\t\t\t"+value[1]+"\t\t\t\t"+value[2])






