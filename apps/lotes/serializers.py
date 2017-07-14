from rest_framework import serializers
from .models import Lotes

class LotesSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Lotes
        fields = ('user', 'name', 'polygon','description','state','region','created_date')
        extra_kwargs = {'user' : {'read_only' : True}}