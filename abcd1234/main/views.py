from django.shortcuts import render
from django.views.generic import ListView
from .models import Coordinates
from django.contrib.gis.geos import Point


class LeafletView(ListView):
    model = Coordinates
    template_name = 'main/leaflet.html'
    context_object_name = 'coordinates'
    extra_context = {
        'title': 'leaflet map',
    }

    def post(self, request):
        if request.method == 'POST' and request.is_ajax():
            query_dict = request.POST
            point = Coordinates()
            pnt = Point(float(query_dict.__getitem__('lat')), float(query_dict.__getitem__('lng')))
            point.location = pnt
            point.save()
        return render(request, self.template_name)
