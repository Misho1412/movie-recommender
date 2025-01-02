import pandas as pd
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, render_template, jsonify
from urllib.parse import quote as url_quote


app = Flask(__name__, static_folder="C:/Users/misho/Downloads/project final/movie-recommender-website/build", static_url_path='/')
    
CORS(app)

def createSimilarity():
    data = pd.read_csv("C:/Users/misho/Downloads/project final/movie-recommender-website/main_data.csv")  # Reading the dataset
    cv = CountVectorizer()
    countMatrix = cv.fit_transform(data['comb'])
    similarity = cosine_similarity(countMatrix)  # Creating the similarity matrix
    return (data, similarity)

def getAllMovies():
    data = pd.read_csv("C:/Users/misho/Downloads/project final/movie-recommender-website/main_data.csv")
    return list(data['movie_title'].str.capitalize())

def  Recommend(movie):
    """
    Recommend movies based on similarity and fallback to TMDB API for missing movies.
    """
    try:
        data.head()
        similarity.shape
    except:
        (data, similarity) = createSimilarity()

    movie = movie.strip().lower()
    movie_titles = data['movie_title'].str.strip().str.lower().unique()

    # Check local dataset first
    if movie in movie_titles:
        movieIndex = data.loc[data['movie_title'].str.lower() == movie].index[0]
        lst = list(enumerate(similarity[movieIndex]))
        lst = sorted(lst, key=lambda x: x[1], reverse=True)
        lst = lst[1:20]  # Exclude the requested movie itself and take the top 20
        movieList = [data['movie_title'][i[0]] for i in lst]
        return movieList

    # If not found locally, fallback to TMDB API
    tmdb_movie = fetch_movie_from_tmdb(movie)
    if tmdb_movie:
        return f"Movie not found locally. Found '{tmdb_movie['title']}' on TMDB with release date {tmdb_movie['release_date']}."
    else:
        return f"Sorry! The movie '{movie}' you requested is not present in our database or TMDB."

@app.route('/api/movies', methods=['GET'])
@cross_origin()
def movies():
    # Returns all the movies in the dataset
    movies = getAllMovies()
    result = {'arr': movies}
    return jsonify(result)

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
        # Return string-based error or TMDB fallback
        return jsonify({'message': recommendations})
    return jsonify({'movies': recommendations})  # Return movie recommendations

@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
