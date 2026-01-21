from .models import (City,Property,District,Region)
from modeltranslation.translator import TranslationOptions,register

@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)

@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('district_name',)

@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('region_name',)

