from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import date
from blog.models import Article

def home_page(request):
    current_date = date.today()
    article = Article.objects.filter(draft=False).order_by('-published_date')
    context = {'date': current_date, 'articles': article}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def root(request):
    return HttpResponseRedirect('home')