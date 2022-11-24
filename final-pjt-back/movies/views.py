from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer, MovieCommentSerializer, LatestListSerializer
from .models import Movie, Latest, MovieComment
import datetime


@api_view(['GET'])
def movie_comments(request):
    comments = get_list_or_404(MovieComment)
    serializer = MovieCommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.moviecomment_set.filter(user=request.user):
        # print(movie.moviecomment_set.all().values('user'))
        for comment in movie.moviecomment_set.all():
            # print(comment.user)
            if comment.user == request.user:
                # print('ok')
                comment.delete()
        serializer = MovieCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        serializer = MovieCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def nowplaying(request) :
    if request.method == 'GET' :
        movies = get_list_or_404(Latest)[:5]
        serializer = LatestListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def top20(request) :
    if request.method == 'GET' :
        movies = get_list_or_404(Movie)
        movies.sort(key = lambda x: x.popularity, reverse=True)
        movies = movies[:20]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def userrecommend(request) :
    movies = get_list_or_404(Movie)
    movies.sort(key = lambda x: x.popularity, reverse=True)
    likegenres = list(request.data.values())
    
    recommend_movie = []
    for movie in movies:
        tmp = []
        # print(list((movie.genres.all().values('name'))))
        for genre in list((movie.genres.all().values('name'))):
            tmp.append(genre['name'])
        if likegenres[0] in tmp or likegenres[1] in tmp or likegenres[2] in tmp:
            recommend_movie.append(movie)
    serializer = MovieListSerializer(recommend_movie[:20], many=True)
    return Response(serializer.data)




@api_view(['GET'])
def timerelated(request) :
    if request.method == 'GET' :
        now = datetime.datetime.now()
        t = ['월', '화', '수', '목', '금', '토', '일']
        r = datetime.datetime.today().weekday()
        movies = get_list_or_404(Movie)
        movies.sort(key = lambda x: x.popularity, reverse=True)
        recommend_movie = []
        # 주말
        # 가족, 애니메이션 영화 추천
        if t[r] == '토' or t[r] == '일':
            for movie in movies:
                tmp = []
                for genre in list((movie.genres.all().values('pk'))):
                    tmp.append(genre['pk'])
                if 10751 in tmp or 16 in tmp or 35 in tmp:
                    recommend_movie.append(movie)
        # 평일
        else:
            # 오전
            # 밤러,에는 호 범죄, 스릴러 추천
            if now.hour <= 6:
                for movie in movies:
                    tmp = []
                    for genre in list((movie.genres.all().values('pk'))):
                        tmp.append(genre['pk'])
                    if 27 in tmp or 80 in tmp or 53 in tmp:
                        recommend_movie.append(movie)
            # 아침시간대에는 다큐멘터리, 드라마, 역사 추천
            elif now.hour <=12:
                for movie in movies:
                    tmp = []
                    # print(list(movie.genres.all().values('pk')))
                    for genre in list((movie.genres.all().values('pk'))):
                        tmp.append(genre['pk'])
                    if 99 in tmp or 18 in tmp or 9648 in tmp:
                        recommend_movie.append(movie)

            # 점심 이후에는 액션, 모험, 공상과학 추천
            elif now.hour <= 18:
                for movie in movies:
                    tmp = []
                    for genre in list((movie.genres.all().values('pk'))):
                        tmp.append(genre['pk'])
                    if 28 in tmp or 12 in tmp or 878 in tmp:
                        recommend_movie.append(movie)
            # 저녁 이후 음악, 로맨스, 판타지 추천
            else:
                for movie in movies:
                    tmp = []
                    for genre in list((movie.genres.all().values('pk'))):
                        tmp.append(genre['pk'])
                    if 10402 in tmp or 10749 in tmp or 14 in tmp:
                        recommend_movie.append(movie)
        recommend_movie = recommend_movie[:20]
        serializer = MovieListSerializer(recommend_movie, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def ssafyplus(request):
    movies = get_list_or_404(Movie)
    ssafyplusmovie = []
    for movie in movies:
        if len(movie.moviecomment_set.all()) >= 5:
            tmp = 0
            for comment in (list(movie.moviecomment_set.all().values('vote_rate'))):
                tmp += comment['vote_rate']
            if tmp / len(movie.moviecomment_set.all()) >= 3.5:
                ssafyplusmovie.append(movie)
            # for comment in list(movie.moviecomment_set.all()):
                
            #     print(comment)
    serializer = MovieListSerializer(ssafyplusmovie, many=True)
    return Response(serializer.data)
