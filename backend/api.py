from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from rest_framework import request, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import LoginSerializer, UserSerializer


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': 'User created, you can log in'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        auth_login(request, user)
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        return Response({'success': 'Login successful', 'user_data': user_data}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    auth_logout(request)
    return Response({'success': 'Logout successful'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def issuperuser(request, id):
    user = User.objects.get(id=id)
    return Response({'issuper': user.is_superuser}, status=status.HTTP_200_OK)
