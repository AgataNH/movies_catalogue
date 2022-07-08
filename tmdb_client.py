import requests

API_TOKEN = "c2c05e38fdd57b4ae0276dfa0bd8d60c"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular?api_key=c2c05e38fdd57b4ae0276dfa0bd8d60c"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c2c05e38fdd57b4ae0276dfa0bd8d60c"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=c2c05e38fdd57b4ae0276dfa0bd8d60c"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]