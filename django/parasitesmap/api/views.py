from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ParasiteSerializer
from .models import Parasite


class ParasiteViewSet(viewsets.ModelViewSet):

    queryset = Parasite.objects.all()
    serializer_class = ParasiteSerializer
    permission_classes = [permissions.IsAuthenticated]