from util import dataUtil
from util import fileUtil

def main():
    movieLines = fileUtil.readLinesFromFile("movie-data/movies/filtered.tsv", "utf8")
    ratingLines = fileUtil.readLinesFromFile("movie-data/ratings/filtered.tsv", "utf8")
    crewLines = fileUtil.readLinesFromFile("movie-data/crew/filtered.tsv", "utf8")
    actorLines = fileUtil.readLinesFromFile("movie-data/roles/actors.tsv", "utf8")
    movies = dataUtil.getMoviesForFileContentOptimized(movieLines, ratingLines, crewLines, actorLines)


if __name__ == "__main__":
    main()