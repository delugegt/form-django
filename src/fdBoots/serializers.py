#aqui5
from django.db.models import fields
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = ('id','code','guest_can_pause','created_at')