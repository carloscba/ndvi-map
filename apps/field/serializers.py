from rest_framework import serializers
from .models import Field

class FieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Field
        fields = ('user', 'name', 'polygon','description','state','region','created_date')