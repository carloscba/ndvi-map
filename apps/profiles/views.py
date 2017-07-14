from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models
from . import serializers
from . import permissions

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    """Test apiview"""
    serializer_class = serializers.ProfilesSerializer
    queryset = models.Profile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self, request):

        return ObtainAuthToken().post(request)