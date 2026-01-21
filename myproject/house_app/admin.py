from django.contrib import admin
from .models import *
from modeltranslation.admin import (
    TranslationAdmin,
    TranslationInlineModelAdmin
)

class PropertyInline( admin.TabularInline):
    model = PropertyImg
    extra = 1


@admin.register(Property)
class PropertyAdmin(TranslationAdmin):
    inlines = [PropertyInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class CityInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = City
    extra = 1

class DistrictInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = District
    extra = 1

@admin.register(Region)
class CityAdmin(TranslationAdmin):
    inlines = [CityInline,DistrictInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    admin.site.register(Review)
    admin.site.register(UserProfile)