from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestCases(TestCase):
    """
    This is the class we will use to test the images
    """
    
    def setUp(self):
        """
        This will create a new image before each test case
        """
        funny = Category(name = "funny")
        funny.save()
        africa = Location(name = "Africa")
        africa.save()
        self.new_image = Image(name = "image",description = "h",location = africa,category = funny)
        self.new_image.save()
    
    def tearDown(self):
        """
        This will clear the db after each test
        """
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_instance(self):
        """
        This will test whether the new image created is an instance of the Image class
        """
        self.assertTrue(isinstance(self.new_image, Image))
    def test_init(self):
        """
        This will test whether the new image is instantiated correctly
        """
        self.assertTrue(self.new_image.name == "image")

    def test_save_image(self):
        """
        This will test whether the new image is added to the db
        """
        g = Image(name = "2")
        g.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)

    def test_delete_image(self):
        """
        This will test whether the new image is deleted from the db
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)
        self.new_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update_image(self):
        """
        This will test whether the image details are updated
        """
        g = Image(name = "hey")
        g.save_image()
        Image.objects.filter(name = "hey").update("bye")
        self.assertTrue(g.name == "bye")

    def test_get_image_by_id(self):
        """
        This will test whether the specific image is queried from the db
        """
        self.new_image.save_image()
        queried_image = Image.get_image_by_id(1)
        self.assertTrue(queried_image.description == "h")

    def test_get_images(self):
        """
        This will test whether the get_image will return all the images
        """
        self.new_image.save_image()
        self.assertTrue(len(Image.get_images()) == 1)

    def test_search_image(self):
        """
        This will test whether the image is queried based on category
        """
        self.assertTrue(len(Image.search_image("funny")) == 1)

    def test_filter_by_location(self):
        """
        This will test whether the filter_by_loc will return photos in a certain category
        """
        self.assertTrue(len(Image.filter_by_location("Africa")) == 1)

