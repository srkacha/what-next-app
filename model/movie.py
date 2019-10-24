#Model for the movie entity
#Created movie has empty lists for crew, actors, genres

class Movie:
    def __init__(self, id, title, year, runtime):
        self.id = id
        self.title = title
        self.year = year
        self.crew = []
        self.actors = []
        self.genres = []
        self.rating = 0

    def addActor(self, actor):
        self.actors.insert(actor)

    def addCrew(self, crew):
        self.crew.insert(crew)

    def addGenre(self, genre):
        self.genres.insert(genre)

    def setRating(self, rating):
        self.rating = rating