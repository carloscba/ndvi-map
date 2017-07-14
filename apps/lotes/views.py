from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .import permissions
from .models import Lotes

class LotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lotes.objects.all()
    serializer_class = serializers.LotesSerializer
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (permissions.UpdateOwnLote, IsAuthenticatedOrReadOnly, IsAuthenticated)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)