"""blog URL Configuration

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

from blog import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.root),
    path('home/', views.home_page, name ='home_page'),
    path('admin/', admin.site.urls),
    path('articles/<int:id>', views.topic_show, name='topic_details'),
    path('comments/new', views.create_comment, name='create_comment'),
    path('article/new', views.create_blog, name='create_article'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('article/edit/<int:id>', views.edit_article, name='edit_article'),
]

