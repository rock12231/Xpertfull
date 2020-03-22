from django.shortcuts import render, redirect
from .models import Slider
from .form import *
from .models import Service
from django.contrib import messages
# Create your views here.

def index(request):
    
    data = Slider.objects.all()
    data2 = Gallery.objects.all()
    data3 = Service.objects.all()
    context = {'data': data, 'data2': data2, 'data3': data3}
    return render(request, "index.html", context)


def image(request):
    data = Slider.objects.all()
    form = SliderForm()
    if request.method == 'POST':
        form = SliderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'data': data, 'form': form}
    return render(request, "images.html", context)

def owner(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('para') and request.POST.get('image'):
            all_data = Service()
            all_data.h3white = request.POST.get('name')
            all_data.para = request.POST.get('para')
            all_data.image = request.POST.get('image')
            all_data.save()
            return render(request, 'index.html')
        else:
            return render(request, 'owner.html')


def owner_data(request):
    data6 = Service.objects.all()
    data5 = Gallery.objects.all()
    data4 = Slider.objects.all()
    context = {'data4': data4, 'data5': data5, 'data6': data6}
    return render(request, "owner.html", context)


def delete(request, pk):
    item = Slider.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'delete.html', context)