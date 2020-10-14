from django.conf.urls import url
from django.conf.urls.static import static
from .  import views
from django.conf import settings

urlpatterns = [
    url(r'^$',views.welcome, name='myPhotos'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^photo/(\d+)',views.photo,name ='photo'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)