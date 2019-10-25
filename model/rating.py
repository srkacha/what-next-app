#Model for rating entity

class Rating:
    def __init__(self, movieId, averageRating, numOfVotes):
        self.movieId = movieId
        self.averageRating =averageRating
        self.numOfVotes = numOfVotes