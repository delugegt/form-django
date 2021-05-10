#aqui 3
from django.urls import path
#from django.urls.resolvers import URLPattern
from .views import RoomView


urlpatterns = [
  path('home', RoomView.as_view()),
  #aqui
  #path('',main)
]