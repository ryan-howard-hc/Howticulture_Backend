from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'
        
class PlantPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantPhoto
        fields = '__all__'

class UserFavoritePlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavoritePlants
        fields = '__all__'