from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FieldSerializer
from .models import Field

class FieldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    #permission_classes = (permissions.IsAuthenticated,)