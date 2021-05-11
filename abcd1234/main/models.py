from django.contrib.gis.db import models


class Coordinates(models.Model):
    location = models.PointField(geography=True)

    @property
    def lat_lng(self):
        return getattr(self.location, 'coords')

    class Meta:
        verbose_name_plural = 'Coordinates'