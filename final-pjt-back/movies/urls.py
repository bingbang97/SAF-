from django.urls import path
from . import views


urlpatterns = [
    path('nowplaying/', views.nowplaying),
    path('top20/', views.top20),
    path('userrecommend/', views.userrecommend),
    path('timerelated/', views.timerelated),
    path('ssafyplus/', views.ssafyplus),
    # 이하 수정
    path('comments/', views.movie_comments),
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('movie/<int:movie_pk>/comments/', views.comment_create),    
]