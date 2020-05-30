"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from tweet.views import (home, compose)
from twitteruser.views import (signup, logout_action)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('compose/', compose, name='compose'),
    path('tweet/<int:id>/', home, name='tweet'),
    # path('user/<str:username>/', user_profile, name='user'),
    path('logout/', logout_action, name='logout'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
