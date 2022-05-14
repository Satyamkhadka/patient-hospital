

# Create your models here.
from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    symptoms = models.TextField(max_length=2000)
    prevention = models.TextField(max_length=2000)
    featured = models.BooleanField()
    display_image = models.ImageField(
        upload_to="disease", max_length=100)
    slider_image1 = models.ImageField(
        upload_to="disease", max_length=100)
    slider_image2 = models.ImageField(
        upload_to="disease", max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.id)+'_'+self.name
