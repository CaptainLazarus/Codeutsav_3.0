from rest_framework import serializers
from startup.models import Startups,Startupprojects,Startupmembers,Investors,Mentors

# Lead Serializer
class StartupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Startups
    fields = '__all__'

class InvestorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Investors
    fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mentors
    fields = '__all__'