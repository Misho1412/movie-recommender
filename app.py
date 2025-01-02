import os
import pandas as pd
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, render_template, jsonify
import requests

# Configurable paths
DATA_PATH = os.getenv("DATA_PATH", "main_data.csv")
STATIC_FOLDER = os.getenv("STATIC_FOLDER", "build")

app = Flask(__name__, static_folder=STATIC_FOLDER, static_url_path='/')
CORS(app)

def createSimilarity():
    data = pd.read_csv(DATA_PATH)
    cv = CountVectorizer()
    countMatrix = cv.fit_transform(data['comb'])
    similarity = cosine_similarity(countMatrix)
    return (data, similarity)

def getAllMovies():
    data = pd.read_csv(DATA_PATH)
    return list(data['movie_title'].str.capitalize())

def fetch_movie_from_tmdb(movie):
    api_key = "your_tmdb_api_key"  # Replace with your TMDB API key
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]
    return None

def Recommend(movie):
    try:
        data.head()
        similarity.shape
    except:
        (data, similarity) = createSimilarity()

    movie = movie.strip().lower()
    movie_titles = data['movie_title'].str.strip().str.lower().unique()

    if movie in movie_titles:
        movieIndex = data.loc[data['movie_title'].str.lower() == movie].index[0]
        lst = list(enumerate(similarity[movieIndex]))
        lst = sorted(lst, key=lambda x: x[1], reverse=True)
        lst = lst[1:20]
        movieList = [data['movie_title'][i[0]] for i in lst]
        return movieList

    tmdb_movie = fetch_movie_from_tmdb(movie)
    if tmdb_movie:
        return f"Movie not found locally. Found '{tmdb_movie['title']}' on TMDB with release date {tmdb_movie['release_date']}."
    else:
        return f"Sorry! The movie '{movie}' you requested is not present in our database or TMDB."

@app.route('/api/movies', methods=['GET'])
@cross_origin()
def movies():
    movies = getAllMovies()
    return jsonify({'movies': movies})

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/similarity/<name>')
@cross_origin()
def similarity(name):
    movie = name
    recommendations = Recommend(movie)
    if isinstance(recommendations, str):
        return jsonify({'error': recommendations})
    return jsonify({'movies': recommendations})

@app.errorhandler(404)
def not_found(e):
    print(f"404 error: {e}")
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
