from django.shortcuts import render
from .forms import EnginForm, DriverForm
from django.http import Http404
from .models import Engin, Driver

# Create your views here.
def engin_list_view(request):
    objs = Engin.objects.all()
    context = {
        'objs':objs    
    }
    return render(request, "engins/index.html", context)

# ENGIN SINLE VIEW
def engin_single_view(request, id):
    try:
        objs  = Engin.objects.get(id=id)
    except Engin.DoesNotExist:
        raise Http404
    context = {
        "objs":objs
    }
    return render(request, "engins/single_eng.html", context)
    
# CREATE ENGIN VIEW
def engin_create_view(request):
    form  = EnginForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context = {
        'form': form
    }
    return render(request, "engins/eng_create.html", context)

# UPDATE VIEW
def engin_update_view(request, id):
    obj = Engin.objects.get(id=id)
    form = EnginForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "engins/update_eng.html", context)

# DELETE VIEW
def engin_del_view(request, id):
    obj = Engin.objects.get(id=id)
    try:
        if request.method == "POST":
            obj.delete()
    except Engin.DoesNotExist:
        raise Http404    
    context = {
        'obj': obj
    }
    return render(request, "engins/eng_del.html")

# ########Driver VIEWS ###########
##################################

# Driver LIST VIEW
def drivers_list_view(request):
    obj = Driver.objects.all

    context = {
        'drivers': obj
    }
    return render(request, "engins/driv_lst.html", context)
    
# VIEW CRATE A DRIVER
def create_driver_view(request):
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context= {
        'form': form
    }
    return render(request, "engins/create_driver.html", context)
    

