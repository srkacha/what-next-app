#Utility functions for working  with lists of movie objects
from util import dataUtil
from util import fileUtil
import numpy as np
from numpy import dot
from numpy.linalg import norm

def loadMovies():
    movieLines = fileUtil.readLinesFromFile("data/movies/filtered.tsv", "utf8")
    ratingLines = fileUtil.readLinesFromFile("data/ratings/filtered.tsv", "utf8")
    crewLines = fileUtil.readLinesFromFile("data/crew/filtered.tsv", "utf8")
    actorLines = fileUtil.readLinesFromFile("data/roles/actors.tsv", "utf8")
    movies = dataUtil.getMoviesForFileContentOptimized(movieLines, ratingLines, crewLines, actorLines)
    return movies

def getMovieForMovieId(movieId):
    for movie in movies:
        if movie.id == movieId:
            return movie
    return None

def generateVectorRepresentationForMovie(movie):
    rep = np.zeros(3)
    rep[0] = float(movie.year)/2020
    rep[1] = float(movie.rating)/10
    rep[2] = float(movie.runtime)/200
    return rep

def loadMovieRepresentations():
    reps = {}
    for movie in movies:
        reps[movie.id] = generateVectorRepresentationForMovie(movie)
    return reps

def getMovieSuggestionsForMovieId(movieId):
    targetMovie = getMovieForMovieId(movieId)
    targetRepresentation = representations[movieId]
    comapreResults = {}
    if not targetMovie: return
    for otherMovie in movies:
        otherMovieCosineSim = dot(targetRepresentation, representations[otherMovie.id])/(norm(targetRepresentation)*norm(representations[otherMovie.id]))
        sameCrewCount = len(set(targetMovie.crew) & set(otherMovie.crew))
        sameGenresCount = len(set(targetMovie.genres) & set(otherMovie.genres))
        sameActorsCount = len(set(targetMovie.actors) & set(otherMovie.actors))
        similarityIndex = otherMovieCosineSim * (1.5**sameCrewCount) * (1.3**sameGenresCount) * (1.2**sameActorsCount)
        comapreResults[otherMovie.id] = similarityIndex
    #now we sort the results
    sortedResults = sorted(comapreResults.items(), key=lambda x: x[1], reverse=True)
    bestResults = sortedResults[1:11]
    resultObjects = generateListOfObjectsBasedOnResults(bestResults)
    return resultObjects

def convertListOfObjectsToListOfDictionaries(movieList):
    dictList = []
    for movie in movieList:
        dictList.append({
            'id': movie.id,
            'title': movie.title,
            'runtime': movie.runtime,
            'year': movie.year,
            'rating': movie.rating,
            'crew': movie.crew,
            'actors': movie.actors,
            'genres': movie.genres,
            'simIndex': movie.simIndex
        })
    return dictList

def generateListOfObjectsBasedOnResults(bestResults):
    movies = []
    for result in bestResults:
        movie = getMovieForMovieId(result[0])
        movie.simIndex = result[1]
        movies.append(movie)
    return movies

#returns first 10 suggestions it finds
def getAutoCompleteSuggestionsBasedOnString(substring):
    low = substring.lower()
    suggestions = []
    foundSuggConter = 0
    for movie in movies:
        if low in movie.title.lower():
            suggestions.append(movie)
            foundSuggConter += 1
            if foundSuggConter == 10: return suggestions
    return suggestions

#exporting variables
movies = loadMovies()
representations = loadMovieRepresentations()

