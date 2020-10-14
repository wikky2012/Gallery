from django.test import TestCase
from django.test import TestCase
from .models import Photo, Category, Location
import datetime as dt


# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.location = Location(name='Kericho')
        self.location.save_location()

        self.category = Category(name='tea')
        self.category.save_category()

        self.image_test = Photo(id=1, name='fifteenTen', description='my best Clone', location=self.location,
                                category=self.category)

        

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Photo))


    def test_save_image(self):
        self.image_test.save_image()
        images = Photo.objects.all()
        self.assertTrue(len(images) > 0) 


    def test_delete_image(self):
        self.new_image = Photo(name = 'fifteenTen', description = 'my best Clone')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Photo.objects.all()
        self.assertEqual(len(images), 0)


    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Photo.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def tearDown(self):
        Photo.objects.all().delete()

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Kericho')
        self.location.save_location()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

   
    def test_update_location(self):
        new_location_name = 'Bomet'
        self.location.update_location(self.location.id,new_location_name)
        changed_location = Location.objects.filter(name='Bomet')
        self.assertTrue(len(changed_location)>0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='tea')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
    
    def test_update_category(self):
        new_category = 'game'
        self.category.update_category(self.category.id, new_category)
        changed_category = Category.objects.filter(name='game')
        self.assertTrue(len(changed_category) > 0)   

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)