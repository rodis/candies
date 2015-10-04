from django.contrib.gis.db import models

class Sweet(models.Model):
        sweet = models.CharField(max_length=140)
        point = models.PointField(srid=4126)
        objects = models.GeoManager()
