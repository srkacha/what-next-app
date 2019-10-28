#Model for the movie entity
#Created movie has empty lists for crew, actors, genres

class Movie:
    def __init__(self, id, title, year, runtime, rating):
        self.id = id
        self.title = title
        self.year = year
        self.runtime = runtime
        self.crew = []
        self.actors = []
        self.genres = []
        self.rating = rating
        self.simIndex = 0

    def setActors(self, actors):
        self.actors = actors

    def setCrew(self, crew):
        self.crew = crew

    def setGenres(self, genres):
        self.genres = genres