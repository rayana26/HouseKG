from django_filters import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'title': ['exact'],
            'region': ['exact'],
            'city': ['exact'],
            'district': ['exact'],
            'price':['gt', 'lt'],
            'area': ['gt', 'lt'],
            'rooms': ['exact'],
            'floor': ['exact'],
            'condition': ['exact'],
            'documents': ['exact']
        }