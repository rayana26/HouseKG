from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Property)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Review)
admin.site.register(PropertyImg)
