import requests
import json

TMDB_API_KEY = '03f9d02e18687131c3ef34a1308a5ee4'

def get_movie_datas():
    total_data = []
    for i in range(1, 11):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            movieId = movie['id']
            request_youtube_url = f"https://api.themoviedb.org/3/movie/{movieId}/videos?api_key={TMDB_API_KEY}"
            youtube_data = requests.get(request_youtube_url).json()
            picture_paths = f"https://api.themoviedb.org/3/movie/{movieId}/images?api_key={TMDB_API_KEY}"
            picture_paths_data = requests.get(picture_paths).json()['backdrops']
            logo_paths_data = requests.get(picture_paths).json()['logos']
            backdrops_path = 'does_not_exists'
            for path in picture_paths_data:
                if path['aspect_ratio'] == 1.778:
                    backdrops_path = path['file_path']
                    break
            if logo_paths_data == []:
                logo_path = 'does_not_exists'
            else:
                logo_path = logo_paths_data[0]['file_path']
            if movie.get('release_date', ''):
                if youtube_data['results'] != []:
                    fields = {
                        'movie_id': movie['id'],
                        'title': movie['title'],
                        'released_date': movie['release_date'],
                        'popularity': movie['popularity'],
                        'vote_avg': movie['vote_average'],
                        'overview': movie['overview'],
                        'poster_path': movie['poster_path'],
                        'genres': movie['genre_ids'],
                        'youtube_id': youtube_data['results'][0]['key'],
                        'related_picture_path' :backdrops_path,
                        'logo_path' : logo_path
                    }
                else:
                    fields = {
                        'movie_id': movie['id'],
                        'title': movie['title'],
                        'released_date': movie['release_date'],
                        'popularity': movie['popularity'],
                        'vote_avg': movie['vote_average'],
                        'overview': movie['overview'],
                        'poster_path': movie['poster_path'],
                        'genres': movie['genre_ids'],
                        'youtube_id': 'does_not_exists',
                        'related_picture_path' : backdrops_path,
                        'logo_path' : logo_path,
                    }
                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)


def get_genre_data():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            # 'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)

    with open("movies/fixtures/genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)


get_movie_datas()
get_genre_data()

'''
movies/fixtures/ 만들고 

python init.py 

python manage.py migrate

python manage.py loaddata genre_data.json movie_data.json

'''