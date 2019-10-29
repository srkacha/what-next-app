from flask import Flask, jsonify
from util import movieUtil
import json
from encoder.movieEncoder import MovieEncoder
import os

app = Flask(__name__)

@app.route('/what-next/api/movies/recommend/<movieId>', methods=['GET'])
def getRecommendationsForMoiveId(movieId):
    movies = movieUtil.getMovieSuggestionsForMovieId(movieId)
    movies = movieUtil.convertListOfObjectsToListOfDictionaries(movies)
    return jsonify({"data": movies})

@app.route('/what-next/api/movies/auto-suggest/<substring>', methods = ['GET'])
def getAutoCompleteBasedOnString(substring):
    autoCompleteSuggestions = movieUtil.getAutoCompleteSuggestionsBasedOnString(substring)
    autoCompleteSuggestions = movieUtil.convertListOfObjectsToListOfDictionaries(autoCompleteSuggestions)
    return jsonify({"data": autoCompleteSuggestions})

if __name__ == "__main__":
    #binding to PORT if defined, othervise defaulting to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port,debug = True)