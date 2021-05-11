from django.urls import path
from .views import LeafletView


urlpatterns = [
    path('', LeafletView.as_view(), name='home'),
]