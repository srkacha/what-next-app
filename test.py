from util import movieUtil

def main():
    suggestions = movieUtil.getMovieSuggestionsForMovieId("tt0110912")
    for s in suggestions:
        movie = movieUtil.getMovieForMovieId(s[0])
        print(movie.title + " " + str(s[1]))

if __name__ == "__main__":
    main()