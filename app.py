from flask import Flask, jsonify
from util import movieUtil
import json
from encoder.movieEncoder import MovieEncoder
import os

app = Flask(__name__)

@app.route('/what-next/api/movies/recommend/<movieId>', methods=['GET'])
def getRecommendationsForMoiveId(movieId):
    movies = movieUtil.getMovieSuggestionsForMovieId(movieId)
    jsonResponse = json.dumps([movie.__dict__ for movie in movies])
    return jsonResponse

@app.route('/what-next/api/movies/auto-suggest/<substring>', methods = ['GET'])
def getAutoCompleteBasedOnString(substring):
    autoCompleteSuggestions = movieUtil.getAutoCompleteSuggestionsBasedOnString(substring)
    jsonResponse = json.dumps([movie.__dict__ for movie in autoCompleteSuggestions])
    return jsonResponse

if __name__ == "__main__":
    #binding to PORT if defined, othervise defaulting to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)