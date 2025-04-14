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
    path('stats-terms', views.show_terms_stats),
    path('stats-examples', views.show_examples_stats)
]
