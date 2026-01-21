from django.urls import path,include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (UserProfileListAPIView,RegionListAPIView,CityListAPIView,ReviewEditView,PropertyListAPIView,DistrictListAPIView,
                    DistrictDetailAPIView,RegionDetailAPIView,CityDetailAPIView,ReviewCreateAPIView,PropertyCreateView,
                    PropertyDetailAPIView,UserProfileDetailAPIView,UserRegisterView,UserLoginView,LogoutView)

router = SimpleRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('property/', PropertyListAPIView.as_view(), name='property_list'),
    path('property/<int:pk>/', PropertyDetailAPIView.as_view(), name='property_detail'),
    path('property_create', PropertyCreateView.as_view(), name='property_generate'),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('review/', ReviewCreateAPIView.as_view(), name='create_review'),
    path('review/<int:pk>/', ReviewEditView.as_view(), name='edit_review'),
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('region/', RegionListAPIView.as_view(), name='region_list'),
    path('region/<int:pk>/', RegionDetailAPIView.as_view(), name='region_detail'),
    path('district/', DistrictListAPIView.as_view(), name='district_list'),
    path('district/<int:pk>/', DistrictDetailAPIView.as_view(), name='district_list'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]