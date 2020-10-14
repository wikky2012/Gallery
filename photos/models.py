from django.db import models
import datetime as dt


class Photo(models.Model):
    name = models.CharField(max_length =60)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'photo/')
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null='True', blank=True)	    
    location = models.ForeignKey('Location', on_delete = models.CASCADE, null='True', blank=True)
    
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()   

    def delete_image(self):
        Photo.objects.filter(id = self.pk).delete() 
    
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value) 

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        image_location = Photo.objects.filter(location__name=location).all()
        return image_location

        
class Category(models.Model):
    name = models.CharField(max_length=15,) 

    def __str__(self):
        return self.name

    @classmethod
    def update_category(cls, id, new_category):
        cls.objects.filter(id=id).update(name=new_category)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()	    


class Location(models.Model):
    name = models.CharField(max_length=20,) 

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

        def __str__(self):
            return self.name

    @classmethod
    def update_location(cls, id, new_location):
        cls.objects.filter(id=id).update(name=new_location)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
