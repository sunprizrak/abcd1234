from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Coordinates


@admin.register(Coordinates)
class CoordinatesAdmin(LeafletGeoAdmin):
    list_display = ('location',)
