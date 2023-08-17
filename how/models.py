from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
    
class Plant(models.Model):
    trefle_id = models.PositiveIntegerField(unique=True)
    common_name = models.CharField(max_length=100, blank=True)
    scientific_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    # author = models.CharField(max_length=100)
    # status = models.CharField(max_length=20)
    # rank = models.CharField(max_length=20)
    family_common_name = models.CharField(max_length=100)
    genus_id = models.PositiveIntegerField()
    observations = models.TextField(blank=True)
    vegetable = models.BooleanField(default=False)
    image_url = models.URLField(max_length=200, blank=True)
    genus = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    foliage_texture = models.CharField(max_length=20, blank=True)
    foliage_color = models.CharField(max_length=20, blank=True)
    leaf_retention = models.BooleanField(default=False)
    fruit_conspicuous = models.BooleanField(default=False)
    fruit_color = models.CharField(max_length=20, blank=True)
    # seed_persistence = models.BooleanField(default=False)
    growth_form = models.CharField(max_length=50, blank=True)
    growth_habit = models.CharField(max_length=50, blank=True)
    growth_rate = models.CharField(max_length=50, blank=True)
    # nitrogen_fixation = models.CharField(max_length=50, blank=True)
    shape_and_orientation = models.CharField(max_length=50, blank=True)
    # toxicity = models.CharField(max_length=50, blank=True)
    # ph_maximum = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    # ph_minimum = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    light = models.PositiveIntegerField(null=True)
    atmospheric_humidity = models.PositiveIntegerField(null=True)
    soil_nutriments = models.PositiveIntegerField(null=True)
    soil_salinity = models.PositiveIntegerField(null=True)
    soil_texture = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.common_name or self.scientific_name

class PlantPhoto(models.Model):
    photo_url = models.URLField(max_length=200)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)