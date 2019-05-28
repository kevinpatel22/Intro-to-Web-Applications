from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import date
from blog.models import Article

def home_page(request):
    current_date = date.today()
    articles = Article.objects.filter(draft=False).order_by('-published_date')
    context = {'date': current_date, 'articles': articles}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def topic_show(request, id):
    article = Article.objects.get(pk=id)
    context = {'article': article}
    response = render(request, 'topic.html', context)
    return HttpResponse(response)

def root(request):
    return HttpResponseRedirect('home')
