from model import movie
import re

#Module for data manipulation utility functions

#Takes movie file content and returns array of movie objects
def getMoviesForFileContent(fileLines):
    movies = []
    for counter, line in enumerate(fileLines):
        if counter == 1: continue
        lineParts = re.split(r'\t+', line)
        id = lineParts[0]
        title = lineParts[2]
        year = lineParts[5]
        runtime = lineParts[7]
        genres = lineParts[8]
        rating = 5
        movies.append(movie.Movie(id, title, year, runtime))
        print(counter)

    return movies
