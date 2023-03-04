"""LoginPremios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.urls import include
from django.conf.urls.static import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/',views.exit,name='Logout'),
    path('',views.Home,name='Home'),
    path('register/',views.register,name='register'),
    path('<int:id>/premios/',views.Premioss,name='Premios'),
    path('<int:id>/obras/',views.Obras, name='Obras'),
    path('cronograma/',views.cronograma, name="cronograma"),
    path('jurado/',views.jurado, name="jurado"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)