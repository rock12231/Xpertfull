from django.shortcuts import render
from images.models import Service
# Create your views here.

def owner(request):
    data6 = Service.objects.all()
    return render(request, "owner.html", {'data6': data6})