
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepg'),
    path('count/',views.count,name='count'),
    path('about/',views.aboutpage,name='aboutpg')
]
