from django.shortcuts import render
from rest_framework import viewsets
from . models import Received, Dispatched
from .serializer import ReceivedSerializer, DispatchedSerializer


class ReceivedViewset(viewsets.ModelViewSet):
    queryset = Received.objects.all()
    serializer_class = ReceivedSerializer


class DispatchedViewset(viewsets.ModelViewSet):
    queryset = Dispatched.objects.all()
    serializer_class = DispatchedSerializer