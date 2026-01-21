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
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class CityInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = City
    extra = 1


@admin.register(Region)
class CityAdmin(TranslationAdmin):
    inlines = [CityInline]

    class Media:
        js = (
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                'modeltranslation/css/tabbed_translation_fields.css',
            ),
        }

    admin.site.register(Review)
    admin.site.register(District)
