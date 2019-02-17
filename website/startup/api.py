from startup.models import Startups,Startupmembers,Startupprojects,Investors,Mentors,OfficeSpaces,Invested,ProgressMilestones
from rest_framework import viewsets, permissions
from .serializers import StartupSerializer,InvestorSerializer,MentorSerializer,spaceSerializer,InvestedSerializer,pmSerializer,supSerializer,sumSerializer
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

class SpaceViewSet(viewsets.ModelViewSet):
    queryset = OfficeSpaces.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = spaceSerializer

class InvestedViewSet(viewsets.ModelViewSet):
    queryset = OfficeSpaces.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = InvestedSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = OfficeSpaces.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = pmSerializer


class supViewSet(viewsets.ModelViewSet):
    queryset = OfficeSpaces.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = supSerializer


class sumViewSet(viewsets.ModelViewSet):
    queryset = OfficeSpaces.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = sumSerializer
    spaceSerializer,InvestedSerializer,pmSerializer,supSerializer,sumSerializer