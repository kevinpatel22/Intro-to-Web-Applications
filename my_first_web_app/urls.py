"""my_first_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

def home_page(request):
    context = {'name': 'Betty Maker'}
    response = render(request, 'index.html')
    return HttpResponse(response)

def portfolio_page(request):
    random_number = randint(0, 100)
    image_url = "https://picsum.photos/800/1000/?image={}".format(random_number)
    context = {'gallery_image': image_url}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

urlpatterns = [
    path('home/', home_page),
    path('portfolio/', portfolio_page)
]
