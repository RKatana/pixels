from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.
def index(request):
    images = Image.get_images()
    
    context = {"images":images}

    return render(request,"index.html",context)

def search(request):
    if "term" in request.GET and request.GET["term"]:
        term = request.GET.get("term")
        photos = Image.search_image(term)
        if photos != "No images found":
            message = "Photos of '" + term + "'"
            return render(request, "search.html", {"images":photos,"message":message,"title":term.capitalize()})
        else:
            message = "No images found"
            return render(request, "search.html", {"images":[],"message":message,"title":term.capitalize()})
    

def locations_page(request):
    return render(request,"locations.html",{"title":"Locations"})

def locations(request,location):

    photos = Image.filter_by_location(location)

    return render(request,"location.html",{"images":photos,"title":location.capitalize()})