from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout as auth_logout

from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import User
from .serializers import UserSerializer


@api_view(['DELETE'])
def signout(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    user.delete()
    auth_logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_all_user(request):
    users = get_list_or_404(User)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)