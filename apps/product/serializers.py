from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    mapid = serializers.CharField(required=True, allow_blank=False, max_length=255)
    token = serializers.CharField(required=True, allow_blank=False, max_length=255)
    array = serializers.CharField(required=True, allow_blank=False)
    downloadUrl = serializers.CharField(required=True, allow_blank=False)
    
