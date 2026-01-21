from django.shortcuts import render
from .serializers import (UserProfileListSerializer,RegionListSerializer,ReviewSerializer,CityListSerializer,
                          DistrictListSerializer,PropertyListSerializer, UserProfileDetailSerializer,PropertyDetailSerializer,
                          PropertyCreateSerializer,DistrictDetailSerializer,RegionDetailSerializer,CityDetailSerializer,
                          ReviewCreateSerializer)
from .models import (UserProfile,Region,Review,City,District,Property)
from rest_framework import viewsets,generics

class UserProfileListAPIView(generics.ListAPIView):
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileListSerializer

  def get_queryset(self):
      return UserProfile.objects.filter(id=self.request.user.id)


class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileDetailSerializer

  def get_queryset(self):
      return UserProfile.objects.filter(id=self.request.user.id)

class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer

class RegionDetailAPIView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDetailSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    # permission_classes = [CheckRolePermission]
    # filterset_fields = ['rating', 'created_date']

class ReviewEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    # permission_classes = [CheckRolePermission]

    def get_queryset(self):
        return Review.objects.filter(buyer=self.request.user)

class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer

class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer

class DistrictListAPIView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictListSerializer

class DistrictDetailAPIView(generics.RetrieveAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictDetailSerializer

class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_class = PropertyFilter
    # search_fields = ['property_type', 'max_guests', 'city',  'rules']
    # pagination_class = PropertyPagination

class PropertyCreateView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyCreateSerializer
    # permission_classes = [CreateHotelPermission]

    def get_queryset(self):
        return Property.objects.filter(seller=self.request.user)


class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer
