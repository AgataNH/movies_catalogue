from main import app
from unittest.mock import Mock
import pytest

def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular?api_key=c2c05e38fdd57b4ae0276dfa0bd8d60c')

@pytest.mark.parametrize('list_type', (
    'popular',
    'now_playing',
    'upcoming',
    'top_rated'
))
def test_list_type(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
       response = client.get('/?list_type={list_type}')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/{list_type}?api_key=c2c05e38fdd57b4ae0276dfa0bd8d60c')
