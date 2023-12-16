from django.contrib import admin
from django.urls import path

from genre.views import index_view, musician_list, musician_detail_view

urlpatterns = [
    path('', index_view, name='index'),
    path('musicians/<slug:genre_slug>/', musician_list, name='musician_list'),
    path('musicians/<slug:slug>/', musician_detail_view, name='musician_detail'),
]
