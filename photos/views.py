from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Photo

# Create your views here.
def welcome(request):
    return render (request, 'all-photos/photo.html')
    

def search_results(request):
    
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos})

def photo(request,photo_id):
    try:
        photo = Photo.objects.get(id = photo_id)
    except ValueError:
        raise Http404()
    return render(request,"all-photo/photo.html", {"photo":photo})