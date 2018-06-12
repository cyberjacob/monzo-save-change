#!/usr/bin/env python
# coding=utf-8
"""monzohosting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar

from monzohosting import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('setup', views.SetupView.as_view(), name="monzo-setup"),
    path('auth', views.AuthView.as_view()),

    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]

for item in os.listdir(settings.APPS_DIR):
    app_name = 'apps.%s' % item
    if item[0] != "_" and os.path.isdir(os.path.join(settings.APPS_DIR, item)) and app_name in settings.INSTALLED_APPS:
        urlpatterns += [path(item+'/', include(app_name+'.urls'))]
