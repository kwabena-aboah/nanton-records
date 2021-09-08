from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from . models import UserProfile, User
from .serializer import UserProfileSerializer, UserSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer