from rest_framework import serializers
from .models import (UserProfile, Property, District, Review, City, Region, PropertyImg)

class UserProfileListSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = ['username', 'email', 'password']


class UserProfileDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = '__all__'

class PropertyCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Property
    fields = '__all__'

class UserProfileNameSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = ['username']

class PropertyImgSerializer(serializers.ModelSerializer):
  class Meta:
    model = PropertyImg
    fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
  class Meta:
    model = District
    fields = ['district_name']

class DistrictListSerializer(serializers.ModelSerializer):
  class Meta:
    model = District
    fields = ['id','district_name']



class ReviewCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = ['city_name']

class CityListSerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = ['id','city_name']

class CityDetailSerializer(serializers.ModelSerializer):
  district_city = DistrictListSerializer(many=True,read_only=True)
  class Meta:
    model = City
    fields = ['city_name','district_city']

class RegionListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = ['id','region_name']

class RegionDetailSerializer(serializers.ModelSerializer):
  city_region = CityListSerializer(many=True,read_only=True)
  class Meta:
    model = Region
    fields = ['region_name','city_region']

class RegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = ['region_name']

class PropertyListSerializer(serializers.ModelSerializer):
  region = RegionSerializer
  city = CitySerializer()
  district = DistrictSerializer()
  property_img = PropertyImgSerializer(many=True,read_only=True)
  class Meta:
    model = Property
    fields = ['id', 'title', 'address', 'area','city','region','district','property_img']

class DistrictDetailSerializer(serializers.ModelSerializer):
  property_place = PropertyListSerializer(many=True, read_only=True)
  class Meta:
    model = District
    fields = ['district_name','property_place']

class PropertyDetailSerializer(serializers.ModelSerializer):
  region = RegionSerializer
  city = CitySerializer()
  district = DistrictSerializer()
  property_img = PropertyImgSerializer(many=True, read_only=True)
  get_avg_rating = serializers.SerializerMethodField()
  count_person = serializers.SerializerMethodField()
  class Meta:
    model = Property
    fields = ['id', 'title', 'address', 'area', 'city', 'region', 'district', 'property_img', 'price','get_avg_rating','count_person']

  def get_avg_rating(self, obj):
      return obj.get_avg_rating()

  def get_count_person(self, obj):
      return obj.get_count_person()


class ReviewSerializer(serializers.ModelSerializer):
  created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%H')
  buyer = UserProfileNameSerializer()
  class Meta:
    model = Review
    fields = ['buyer', 'comment', 'rating', 'created_date']