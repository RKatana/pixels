from django.db import models

# Create your models here.
class Location(models.Model):
    """
    This is the class where we will create locations
    """
    name = models.CharField(max_length = 30)


class Category(models.Model):
    """
    This is the class where we will create categories
    """
    name = models.CharField(max_length = 30)

class Image(models.Model):
    """
    This is the class we will use toc reate images
    """
    image_url = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 40)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)



