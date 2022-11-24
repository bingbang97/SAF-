import requests
import json

TMDB_API_KEY = '03f9d02e18687131c3ef34a1308a5ee4'

def get_latest_movie():
    total_data = []
    
    request_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=ko-KR&page=1"
    movies = requests.get(request_url).json()
    for movie in movies['results']:
        movieId = movie['id']
        request_youtube_url = f"https://api.themoviedb.org/3/movie/{movieId}/videos?api_key={TMDB_API_KEY}"
        youtube_data = requests.get(request_youtube_url).json()
        # picture_paths = f"https://api.themoviedb.org/3/movie/{movieId}/images?api_key={TMDB_API_KEY}"
        # picture_paths_data = requests.get(picture_paths).json()['backdrops']
        # backdrops_path = 'does_not_exists'
        # for path in picture_paths_data:
        #     if path['aspect_ratio'] == 1.778:
        #         backdrops_path = path['file_path']
        #         break
        if movie.get('release_date', ''):
            if youtube_data['results'] != []:
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'genres': movie['genre_ids'],
                    'youtube_id': youtube_data['results'][0]['key'],
                    # 'related_picture_path' :backdrops_path
                }
            else:
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'genres': movie['genre_ids'],
                    'youtube_id': 'does_not_exists',
                    # 'related_picture_path' :backdrops_path
                }

            data = {
                "pk": movie['id'],
                "model": "movies.latest",
                "fields": fields
            }

            total_data.append(data)

    with open("movies/fixtures/latest_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)



get_latest_movie()

'''
movies/fixtures/ 만들고 

python init.py 

python manage.py migrate

python manage.py loaddata genre_data.json movie_data.json

'''