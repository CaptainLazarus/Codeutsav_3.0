from rest_framework import serializers
from startup.models import Startups,Startupprojects,Startupmembers,Investors,Mentors,ProgressMilestones,OfficeSpaces,Invested

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

class supSerializer(serializers.ModelSerializer):
  class Meta:
    model = Startupprojects
    fields = '__all__'

class sumSerializer(serializers.ModelSerializer):
  class Meta:
    model = Startupmembers
    fields = '__all__'

class pmSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProgressMilestones
    fields = '__all__'

class spaceSerializer(serializers.ModelSerializer):
  class Meta:
    model = OfficeSpaces
    fields = '__all__'

class InvestedSerializer(serializers.ModelSerializer):
  class Meta:
    model = Invested
    fields = '__all__'

    