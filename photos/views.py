from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.
def index(request):
    images = Image.get_images()

    three_images_list = [images[x:x+3] for x in range(0, len(images),3)]


    context = {"images":images}

    return render(request,"index.html",context)

def search(request):
    if "term" in request.GET and request.GET["term"]:
        term = request.GET.get("term")
        photos = Image.search_image(term)
        return render(request, "search.html", {"images":photos})
def locations_page(request):
    return render(request,"locations.html")

def locations(request,location):

    photos = Image.filter_by_location(location)

    return render(request,"location.html",{"images":photos,"title":location})