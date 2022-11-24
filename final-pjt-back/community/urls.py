from django.urls import path
from . import views


urlpatterns = [
    path('community/', views.article_list),
    path('community/<int:article_pk>/', views.article_detail),
    path('community/<int:article_pk>/likes/', views.article_likes),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('community/<int:article_pk>/comments/', views.comment_create),
]