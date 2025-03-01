"""sds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', include('solubility.urls')),
    path('admin/', admin.site.urls),
    path('authors/', include('authors.urls')),
    path('journals/', lambda req: redirect('/')),
    path('references/', include('references.urls')),
    path('reports/', include('reports.urls')),
    path('substances/', include('substances.urls')),
    path('systems/', include('systems.urls')),
    path('volumes/', include('volumes.urls')),
    path('viewer/', include('viewer.urls')),
    path('users/', include('users.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
