#Utility functions for working  with lists of movie objects
from util import dataUtil
from util import fileUtil
import numpy as np
from numpy import dot
from numpy.linalg import norm

def loadMovies():
    movieLines = fileUtil.readLinesFromFile("movie-data/movies/filtered.tsv", "utf8")
    ratingLines = fileUtil.readLinesFromFile("movie-data/ratings/filtered.tsv", "utf8")
    crewLines = fileUtil.readLinesFromFile("movie-data/crew/filtered.tsv", "utf8")
    actorLines = fileUtil.readLinesFromFile("movie-data/roles/actors.tsv", "utf8")
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
    return bestResults




#exporting variables
movies = loadMovies()
representations = loadMovieRepresentations()

