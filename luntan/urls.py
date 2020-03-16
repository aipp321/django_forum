"""luntan URL Configuration

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
from forum import views as forum_view
from login import views as login_view
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', forum_view.forum_show),
    path('login/', login_view.login),
    path('register/', login_view.register),
    path('', login_view.register),
    path('captcha/', include('captcha.urls')),
    path('confirm/',login_view.user_confirm),
    path('logout/',login_view.logout),
]
