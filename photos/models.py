from django.db import models

# Create your models here.
class Location(models.Model):
    """
    This is the class where we will create locations
    """
    name = models.CharField(max_length = 30)

    def save_location(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        Location.objects.get(id = self.id).delete()

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Location.objects.get(id = self.id).update(field = val)

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    This is the class where we will create categories
    """
    name = models.CharField(max_length = 30)
    def save_location(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        Location.objects.get(id = self.id).delete()

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Location.objects.get(id = self.id).update(field = val)

    def __str__(self):
        return self.name
class Image(models.Model):
    """
    This is the class we will use to create images
    """
    image_url = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def save_image(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete_image(self):
        """
        This is the function that we will use to delete the instance of this class
        """
        Image.objects.get(id = self.id).delete()

    def update_image(self,field,val):
        """
        This is the method to update the instance
        """
        Image.objects.get(id = self.id).update(field = val)

    @classmethod
    def get_image_by_id(cls,id):
        """
        This is the method to get a specific image
        """
        return cls.objects.get(id = id)

    @classmethod
    def get_images(cls):
        return cls.objects.all()

    @classmethod
    def search_image(cls,category):
        """
        This is the method to search images based on a specific category
        """
        searched_category = Category.objects.get(name  = category)

        return cls.objects.filter(category_id = searched_category.id)

    @classmethod
    def filter_by_location(cls,location):
        """
        This is the method to get images taken in a certain location
        """
        return cls.objects.filter(location = location)
    def __str__(self):
        return self.name
