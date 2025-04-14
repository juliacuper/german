"""
URL configuration for the German app.

This module defines the URL patterns for the German app,
including views for listing terms and examples, adding new entries,
and displaying statistics.
"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('terms-list', views.terms_list),
    path('examples-list', views.examples_list),
    path('add-term', views.add_term),
    path('add-example', views.add_example),
    path('send-term', views.send_term),
    path('send-example', views.send_example),
    path('stats', views.show_stats)
]
