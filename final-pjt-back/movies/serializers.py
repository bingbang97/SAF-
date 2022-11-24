from rest_framework import serializers
from .models import Movie, MovieComment, UserGenre, Latest


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class LatestListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Latest
        fields = '__all__'

class MovieCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    moviename = serializers.CharField(source='movie.title', read_only=True)
    movie_poster = serializers.CharField(source='movie.poster_path', read_only=True)
    
    class Meta:
        model = MovieComment
        fields = '__all__'
        read_only_fields = ('movie', 'user')

    
class MovieSerializer(serializers.ModelSerializer):
    moviecomment_set = MovieCommentSerializer(many=True, read_only=True)
    moviecomment_count = serializers.IntegerField(source='moviecomment_set.count', read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

class UserGenreSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserGenre
        fields = ('genres')
