from util import dataUtil
from util import fileUtil

ratingFitlerThreshold = 10000
doFilter = False

def main():
    if doFilter:
        filterRatings(ratingFitlerThreshold)
        filterMoviesFromAllTypes()
        filterMoviesBasedOnRatingsFile()
        filterCrewBasedOnMoviesFile()
        filterRolesBasedOnMoviesFile()
        fitlerActorsFromRoles()
        print("Filtering done!")
    else:
        print("Filtering disabled!")

def filterRatings(threshold):
    ratingLines = fileUtil.readLinesFromFile("movie-data/ratings/data.tsv", "utf8")
    res = dataUtil.filterRatingsLowerThat(ratingLines, threshold)
    if res > 0:
        print("Fitlered out " + str(res) + " ratings sucessfully")
    else:
        print("Error filtering out ratings")

def filterMoviesFromAllTypes():
    fileLines = fileUtil.readLinesFromFile("movie-data/movies/data.tsv", "utf8")
    res = dataUtil.filterMoviesFromAllTypes(fileLines)
    if res > 0:
        print("Fitlered out " + str(res) + " movies sucessfully")
    else:
        print("Error filtering out ratings")

def filterMoviesBasedOnRatingsFile():
    movieLines = fileUtil.readLinesFromFile("movie-data/movies/movies.tsv", "utf8")
    ratingLines = fileUtil.readLinesFromFile("movie-data/ratings/filtered.tsv", "utf8")
    res = dataUtil.filterMoviesBasedOnRatingsFile(movieLines, ratingLines)
    if res > 0:
        print("Fitlered out " + str(res) + " movies based on rating file sucessfully")
    else:
        print("Error filtering out ratings")

def filterCrewBasedOnMoviesFile():
    movieLines = fileUtil.readLinesFromFile("movie-data/movies/filtered.tsv", "utf8")
    crewLines = fileUtil.readLinesFromFile("movie-data/crew/data.tsv", "utf8")
    res = dataUtil.filterCrewBasedOnMoviesFile(movieLines, crewLines)
    if res > 0:
        print("Fitlered out " + str(res) + " crew based on movie file sucessfully")
    else:
        print("Error filtering out ratings")

def filterRolesBasedOnMoviesFile():
    movieLines = fileUtil.readLinesFromFile("movie-data/movies/filtered.tsv", "utf8")
    res = dataUtil.filterRolesBasedOnMoviesFile(movieLines)
    if res > 0:
        print("Fitlered out " + str(res) + " roles based on movie file sucessfully")
    else:
        print("Error filtering out ratings")

def fitlerActorsFromRoles():
    roleLines = fileUtil.readLinesFromFile("movie-data/roles/filtered.tsv", "utf8")
    res = dataUtil.filterActorsFromAllRoles(roleLines)
    if res > 0:
        print("Fitlered out " + str(res) + " actors based on roles file sucessfully")
    else:
        print("Error filtering out ratings")


if __name__ == "__main__":
    main()