import requests
from django.shortcuts import render
from rest_framework import viewsets, status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

@api_view(['GET'])
def plant_list(request):
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

class PlantPhotoList(APIView):
    def get(self, request):
        photos = PlantPhoto.objects.all()
        serializer = PlantPhotoSerializer(photos, many=True)
        return Response(serializer.data)
    
class UserFavoritePlantsList(APIView):
    def get(self, request):
        favorite_plants = UserFavoritePlants.objects.all()
        serializer = UserFavoritePlantsSerializer(favorite_plants, many=True)
        return Response(serializer.data)