from rest_framework import serializers
from .models import (UserProfile,Property,District,Review,City,Region)

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
  class Meta:
    model = Property
    fields = '__all__'

class DistrictUserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = District
    fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = '__all__'