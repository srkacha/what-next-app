from util import dataUtil
from util import fileUtil

#Main function
def main():
    movieFileLines = fileUtil.readLinesFromFile("movie-data/movies/data.tsv", "utf8")
    movies = dataUtil.getMoviesForFileContent(movieFileLines)
    print(movies[0])


if __name__ == "__main__":
    main()