from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.
def index(request):

    context = {"images":Image.get_images()}

    return render(request,"index.html",context)