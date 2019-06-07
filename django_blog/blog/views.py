from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from django.views.decorators.http import require_http_methods
from .models import Article, Comment
from .forms import ArticleModelForm, LoginForm

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

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.user = request.user
            new_blog.save()
            return redirect('topic_details', id=new_blog.id)
    else:
        form = ArticleModelForm()
    html_response = render(request, 'create_article.html', {'form': form})
    return HttpResponse(html_response)

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()
    context = {'form': form}
    http_response = render(request, 'login.html', context)
    return HttpResponse(http_response)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home')
    else:
        form = UserCreationForm()
    html_response = render(request, 'signup.html', {'form': form})
    return HttpResponse(html_response)

@login_required
def edit_article(request, id):
    edit = get_object_or_404(Article, pk=id, user=request.user.pk)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('topic_details', id=edit.id)
    else:
        form = ArticleModelForm(instance=edit)
    html_response = render(request, 'edit_article.html', {'form': form, 'edit': edit})
    return HttpResponse(html_response)
