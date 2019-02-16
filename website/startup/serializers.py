from rest_framework import serializers
from startup.models import Team 

# Lead Serializer
class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team 
    fields = '__all__'