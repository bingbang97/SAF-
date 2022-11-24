from django.urls import path
from . import views


urlpatterns = [
    path('signount/<int:user_pk>/', views.signout),
    path('getallusers/', views.get_all_user),
    path('userinfo/<int:user_pk>/', views.get_user),
]