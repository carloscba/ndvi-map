from rest_framework import serializers
from . import models

class ProfilesSerializer(serializers.ModelSerializer):
    """A serializer for user profile objects"""
    #name = serializers.CharField(max_length=10)

    class Meta:
        model = models.Profile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        user = models.Profile(
            email = validated_data['email'],
            name = validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user