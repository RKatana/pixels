web: gunicorn pixels.wsgi


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


