import tmdb_client
from unittest.mock import Mock

def test_get_single_movie(monkeypatch):
    mock_movie = ['Movie 1']
    
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    
    movies_list = tmdb_client.get_single_movie(movie_id = 1)
    assert movies_list == mock_movie

def test_get_single_movie_cast(monkeypatch):
    mock_cast = ['Cast']

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_cast
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie_cast = tmdb_client.get_single_movie_cast(movie_id = 1)
    assert movie_cast == mock_cast

