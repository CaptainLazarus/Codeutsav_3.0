from startup.models import Team
from rest_framework import viewsets, permissions
from .serializers import TeamSerializer

# Lead Viewset


class UserViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = TeamSerializer