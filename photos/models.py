from django.db import models
import datetime as dt


class Photo(models.Model):
    category = models.CharField(max_length =60)
    location = models.CharField(max_length =60)
    image = models.ImageField(upload_to = 'photo/')
    
    def __str__(self):
        return self.category

    class meta:
        ordering =['name']
    
    def save_photo(self):
        self.save()


    @classmethod
    def search_by_category(cls,search_term):
        news = cls.objects.filter(category__icontains=search_term)
        return news
        
    
