from startup.models import Startups,Startupmembers,Startupprojects,Investors,Mentors
from rest_framework import viewsets, permissions
from .serializers import StartupSerializer,InvestorSerializer,MentorSerializer
# Lead Viewset

class StartupsViewSet(viewsets.ModelViewSet):
    queryset = Startups.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = StartupSerializer

class InvestorsViewSet(viewsets.ModelViewSet):
    queryset = Investors.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = InvestorSerializer

class MentorsViewSet(viewsets.ModelViewSet):
    queryset = Mentors.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = MentorSerializer