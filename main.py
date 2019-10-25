from util import dataUtil
from util import fileUtil

#Main function
def main():
    movieFileLines = fileUtil.readLinesFromFile("movie-data/movies/filtered.tsv", "utf8")
    ratingFileLines = fileUtil.readLinesFromFile("movie-data/ratings/filtered.tsv", "utf8")
    print(len(movieFileLines) == len(ratingFileLines))


if __name__ == "__main__":
    main()