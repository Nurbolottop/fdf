from django.shortcuts import render
from apps.base.models import Settings,Banner,Numbers

# Create your views here.

def index(request):
    settings = Settings.objects.first()
    banner = Banner.objects.first()
    numbers = Numbers.objects.first()
    return render(request,"index.html",locals())

def about(request):
    settings = Settings.objects.first()
    return render(request,"about.html",locals())


def contacts(request):
    settings = Settings.objects.first()
    return render(request,'contacts.html',locals())