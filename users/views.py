from django.shortcuts import render
from rest_framework import viewsets
from . models import UserProfile
from .serializer import UserProfileSerializer


class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer