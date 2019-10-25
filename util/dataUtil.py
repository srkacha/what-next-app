from model import movie
from model import rating
import re

#Module for data manipulation utility functions

#Takes movie file content and returns array of movie objects
def getMoviesForFileContent(movieLines, ratingLines, crewLines, actorLines):
    movies = []
    for counter, line in enumerate(movieLines):
        if counter == 0: continue
        lineParts = re.split(r'\t+', line)
        id = lineParts[0]
        title = lineParts[2]
        year = lineParts[5]
        runtime = lineParts[7]
        genres = lineParts[8]
        rating = getRatingForMovieId(id, ratingLines)

        newmovie = movie.Movie(id, title, year, runtime, rating)
        newmovie.setGenres(generateGenresList(genres))
        newmovie.setCrew(getCrewForMovieId(id, crewLines))
        newmovie.setActors(getActorsForMovieId(id, actorLines))
        movies.append(newmovie)
        print(counter)
    return movies

#Previous way of building the movie list was too slow cause it was iterating from the start of the actor, crew and rating lists for every movie
#This implementation goes along every list shoulder to shoulder so it should work a bit faster, only iterates one through every list
def getMoviesForFileContentOptimized(movieLines, ratingLines, crewLines, actorLines):
    movieCounter = 0
    ratingCounter = 0
    crewCounter = 0
    actorCounter = 0
    movieLinesLen = len(movieLines)
    movies = []
    while movieCounter < movieLinesLen:
        movieParts = re.split(r'\t+', movieLines[movieCounter])
        id = movieParts[0]
        title = movieParts[2]
        year = movieParts[5]
        runtime = movieParts[7]
        genres = generateGenresList(movieParts[8])
        rating = 0
        crew = []
        actors =[]

        #finding the apropriate rating for the current movie iteration
        while True:
            if ratingCounter == len(ratingLines) - 1: break
            ratingParts = re.split(r'\t+', ratingLines[ratingCounter])
            ratingMovieId = ratingParts[0]
            if ratingMovieId < id:
                ratingCounter += 1
            elif ratingMovieId == id:
                rating = ratingParts[1]
                break
            else:
                rating = 0
                break

        #finding the apropriate crew memberes for the current movie iteration
        while True:
            if crewCounter == len(crewLines) - 1: break
            crewParts = re.split(r'\t+', crewLines[crewCounter])
            crewMovieId = crewParts[0]
            if crewMovieId < id:
                crewCounter += 1
            elif crewMovieId == id:
                directors = re.split(r',', crewParts[1])
                writers = re.split(r',', crewParts[2])
                crew = directors + writers
                break
            else:
                crew = []
                break

        #finding the apropriate actors for the current movie iteration
        while True:
            if actorCounter == len(actorLines) - 1: break
            actorParts = re.split(r'\t+', actorLines[actorCounter])
            actorMovieId = actorParts[0]
            if actorMovieId < id:
                actorCounter += 1
            elif actorMovieId == id:
                actors.append(actorParts[2])
                actorCounter += 1
            else:
                break

        newMovie = movie.Movie(id, title, year, runtime, rating)
        newMovie.setActors(actors)
        newMovie.setCrew(crew)
        movies.append(newMovie)

        movieCounter += 1
        print(movieCounter)

    return movies

def getRatingForMovieId(movieId, ratingLines):
    for line in ratingLines:
        lineParts = re.split(r'\t+', line)
        if lineParts[0] == movieId:
            return lineParts[1]
    #if the movie is not found
    return 0

def getCrewForMovieId(movieId, crewLines):
    for line in crewLines:
        lineParts = re.split(r'\t+', line)
        if lineParts[0] == movieId:
            directors = lineParts[1]
            writers = lineParts[2]
            directors = re.split(r',', directors)
            writers = re.split(r',', writers)
            return directors + writers

def getActorsForMovieId(movieId, actorLines):
    actors = []
    for line in actorLines:
        lineParts = re.split(r'\t+', line)
        if lineParts[0] == movieId:
            actors.append(lineParts[2])
        if lineParts[0] > movieId:
            return actors

def generateGenresList(genresString):
    genres = re.split(r',', genresString)
    return genres

#Takes rating file content and returns array of rating objects
def getRatingsForFileContent(fileLines):
    ratings = []
    for counter, line in enumerate(fileLines):
        if counter == 0: continue
        lineParts = re.split(r'\t+', line)
        movieId = lineParts[0]
        averageRating = lineParts[1]
        numOfVotes = lineParts[2]
        ratings.append(rating.Rating(movieId, averageRating, numOfVotes))

    return ratings

#Used for filtering out ratings lower that some threshold, writes new ratigns to file
def filterRatingsLowerThat(ratingLines, threshold):
    fitleredLines = 0
    filteredFileHandle = open("movie-data/ratings/filtered.tsv", encoding="utf8", mode='w')
    if filteredFileHandle.mode == 'w':
        for counter, line in enumerate(ratingLines):
            if counter == 0 : continue
            lineParts = re.split(r'\t+', line)
            numOfVotes = lineParts[2]
            if int(numOfVotes) > threshold:
                filteredFileHandle.write(line)
                fitleredLines += 1
        return fitleredLines

    else:
        return 0

def filterMoviesFromAllTypes(fileLines):
    fitleredLines = 0
    filteredFileHandle = open("movie-data/movies/movies.tsv", encoding="utf8", mode='w')
    if filteredFileHandle.mode == 'w':
        for counter, line in enumerate(fileLines):
            if counter == 0 : continue
            lineParts = re.split(r'\t+', line)
            type = lineParts[1]
            if type == 'movie':
                filteredFileHandle.write(line)
                fitleredLines += 1
        return fitleredLines

    else:
        return 0

def filterMoviesBasedOnRatingsFile(movieLines, ratingLines):
    filteredLines = 0
    filteredFileHandle = open("movie-data/movies/filtered.tsv", encoding="utf8", mode='w')
    movieCounter = 1
    ratingCounter = 1
    ratingLinesLen = len(ratingLines)
    while ratingCounter < ratingLinesLen:
        movieLine = movieLines[movieCounter]
        ratingLine = ratingLines[ratingCounter]
        movieLineId = re.split(r'\t+', movieLine)[0]
        ratingLineMovieId = re.split(r'\t+', ratingLine)[0]
        if ratingLineMovieId < movieLineId:
            ratingCounter += 1
        elif ratingLineMovieId > movieLineId:
            movieCounter += 1
        elif ratingLineMovieId == movieLineId:
            filteredFileHandle.write(movieLine)
            ratingCounter += 1
            movieCounter += 1
            filteredLines += 1

    return filteredLines

def filterCrewBasedOnMoviesFile(movieLines, crewLines):
    filteredLines = 0
    filteredFileHandle = open("movie-data/crew/filtered.tsv", encoding="utf8", mode='w')
    movieCounter = 1
    crewCounter = 1
    movieLinesLen = len(movieLines)
    while movieCounter < movieLinesLen:
        movieLine = movieLines[movieCounter]
        crewLine = crewLines[crewCounter]
        movieLineId = re.split(r'\t+', movieLine)[0]
        crewLineMovieId = re.split(r'\t+', crewLine)[0]
        if crewLineMovieId < movieLineId:
            crewCounter += 1
        elif crewLineMovieId > movieLineId:
            movieCounter += 1
        elif crewLineMovieId == movieLineId:
            filteredFileHandle.write(crewLine)
            crewCounter += 1
            movieCounter += 1
            filteredLines += 1
    return filteredLines

#Roles file is huge so we will read the lines one by one in this case
def filterRolesBasedOnMoviesFile(movieLines):
    filteredLines = 0
    filteredFileHandle = open("movie-data/roles/filtered.tsv", encoding="utf8", mode='w')
    movieCounter = 1
    roleCounter = 1
    movieLinesLen = len(movieLines)

    with open("movie-data/roles/data.tsv", encoding="utf8", mode='r') as roleFile:
        for roleLine in roleFile:
            if movieCounter == (movieLinesLen - 1): break
            movieLine = movieLines[movieCounter]
            movieLineId = re.split(r'\t+', movieLine)[0]
            roleLineMovieId = re.split(r'\t+', roleLine)[0]
            if roleLineMovieId == movieLineId:
                filteredFileHandle.write(roleLine)
                filteredLines += 1
            while roleLineMovieId > movieLineId:
                movieCounter += 1
                movieLine = movieLines[movieCounter]
                movieLineId = re.split(r'\t+', movieLine)[0]
            print(movieCounter)
    return filteredLines

def filterActorsFromAllRoles(fileLines):
    fitleredLines = 0
    filteredFileHandle = open("movie-data/roles/actors.tsv", encoding="utf8", mode='w')
    if filteredFileHandle.mode == 'w':
        for counter, line in enumerate(fileLines):
            if counter == 0 : continue
            lineParts = re.split(r'\t+', line)
            type = lineParts[3]
            if type == 'actor' or type == 'actress':
                filteredFileHandle.write(line)
                fitleredLines += 1
        return fitleredLines

    else:
        return 0