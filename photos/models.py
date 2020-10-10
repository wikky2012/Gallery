from django.db import models
import datetime as dt


class Photo(models.Model):
    title = models.CharField(max_length =60)
    location = models.CharField(max_length =60)
    my_image = models.ImageField(upload_to = 'photo/')
    
    def __str__(self):
        return self.title


    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
        
    
