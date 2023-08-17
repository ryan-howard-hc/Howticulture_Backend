from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from .views import *

app_name = 'how'

router = routers.DefaultRouter()
# Define router.register(...) for other viewsets if needed

urlpatterns = [
    path('', include(router.urls)),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('plant-list/', plant_list, name='plant-list'),
    path('plant-photos/', PlantPhotoList.as_view(), name='plant-photo-list'),
    path('user-favorite-plants/', UserFavoritePlantsList.as_view(), name='user-favorite-plants-list'),
    path('user-notifications/', UserNotificationList.as_view(), name='user-notification-list'),

]