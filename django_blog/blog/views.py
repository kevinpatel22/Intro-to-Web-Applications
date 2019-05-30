from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import date
from django.views.decorators.http import require_http_methods
from blog.models import Article, Comment

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

@require_http_methods(['POST'])
def create_comment(request):
    user_name = request.POST['name']
    user_message = request.POST['message']
    user_select_article = request.POST['article']
    select_article = Article.objects.get(id=user_select_article)
    comment = Comment(name=user_name, article=select_article, message=user_message)
    comment.save()
    return redirect("topic_details", id=user_select_article)
