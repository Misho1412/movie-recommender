import pytest
from app import createSimilarity, getAllMovies, Recommend, app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_similarity():
    data, similarity = createSimilarity()
    assert data is not None
    assert similarity.shape[0] == len(data)

def test_get_all_movies():
    movies = getAllMovies()
    assert len(movies) > 0
    assert all(isinstance(movie, str) for movie in movies)

def test_recommend_valid():
    data, _ = createSimilarity()
    movie = data['movie_title'].iloc[0]
    result = Recommend(movie)
    assert isinstance(result, list)

def test_recommend_invalid():
    result = Recommend("Nonexistent Movie")
    assert isinstance(result, str)
    assert "not present in our database" in result

def test_api_movies(client):
    response = client.get('/api/movies')
    assert response.status_code == 200
    assert "movies" in response.json
