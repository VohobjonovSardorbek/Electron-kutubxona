"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tkinter.font import names

from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bosh_sahifa_view, name="bosh sahifa"),
    path('bolimlar/', bolimlar_view, name="bolimlar"),
    path('mualliflar/', mualliflar_view, name="mualliflar"),
    path('kitoblar/', kitoblar_view, name="kitoblar"),
    path('kitoblar/<int:pk>/', kitob_details_view),
    path('yangi_asarlar/', yangi_asarlar_view),
    path('kitob/qoshish/', kitob_qoshish_view),
    path("kitob/<int:pk>/o'chirish/", kitob_detele_view),
]
