from django.shortcuts import render

# Create your views here.
#aqui1
from rest_framework import generics 
from .serializers import RoomSerializer 
from .models import Room

class RoomView(generics.CreateAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer