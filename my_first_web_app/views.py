from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home_page(request):
    context = {'name': 'Betty Maker'}
    response = render(request, 'index.html')
    return HttpResponse(response)

def portfolio_page(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0, 100)
        image_urls.append("https://picsum.photos/800/1000/?image={}".format(random_number))
    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me_page(request):
    context = {'skills': ['Python', 'HTML', 'CSS','Django'], 'interests': ['Business', 'Travel']}
    response = render(request,'about.html', context)
    return HttpResponse(response)

def favorites_page(request):
    link = 'https://sites.google.com/generalassemb.ly/gatorontooutcomes/home'
    context = {'fave_links': link}
    response = render(request, 'favourites.html', context)
    return HttpResponse(response)

def root(request):
    return HttpResponseRedirect('home')

def gallery(request):
    return HttpResponseRedirect('/portfolio')