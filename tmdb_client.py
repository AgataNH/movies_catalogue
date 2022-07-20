import requests

API_TOKEN = "c2c05e38fdd57b4ae0276dfa0bd8d60c"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_popular_movies():
    return call_tmdb_api(f"movie/popular?api_key={API_TOKEN}")

def get_movies_list(list_type):
   return call_tmdb_api(f"movie/{list_type}?api_key={API_TOKEN}")

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}?api_key={API_TOKEN}")

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_TOKEN}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]
