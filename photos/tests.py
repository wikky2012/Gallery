from django.test import TestCase
from django.test import TestCase
from .models import Photo
import datetime as dt

# Create your tests here.
class PhotoTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.sport= Photo(category = 'sport', location ='Nairobi')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sport,Photo))
    # Testing Save Method
    def test_save_method(self):
        self.sport.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > -1)


    def tearDown(self):
        Photo.objects.all().delete()
       
    
    