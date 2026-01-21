from django.db import models
from  django.contrib.auth.models import  AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    RoleChoices = (
    ('seller', 'seller'),
    ('buyer', 'buyer')
    )
    user_role = models.CharField(max_length=30, choices=RoleChoices,default='buyer')
    phone_number = PhoneNumberField(null=True, blank=True)
    avatar = models.ImageField(upload_to='user_photo', null=True, blank=True)

    def __str__(self):
        return f'{self.username}, {self.password}, {self.email}'

class Region(models.Model):
    region_name = models.CharField(max_length=30)

    def __str__(self):
        return self.region_name

class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE,related_name='city_region')
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.city_name


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='district_city')
    district_name = models.CharField(max_length=30)

    def __str__(self):
        return self.district_name

class Property(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='property_place')
    address = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.PositiveSmallIntegerField(default=True)
    rooms = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    total_floors = models.PositiveSmallIntegerField()
    condition = models.CharField(max_length=100)
    documents = models.BooleanField()
    video = models.ImageField(upload_to='video_photo', null=True, blank=True)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title},{self.descriptions},{self.region},{self.city},{self.seller}'


    def get_avg_rating(self):
        reviews = self.review_property.all()
        if reviews.exists():
            return round(sum([i.rating for i in reviews]) / reviews.count(), 1)
        return 0

    def get_count_person(self):
         return self.review_property.count()


class PropertyImg(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_img')
    property_img = models.ImageField(upload_to='property_photo')

    def __str__(self):
        return f'{self.property}, {self.property_img}'

class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='review_property')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1,6)])
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.buyer},{self.rating}'


