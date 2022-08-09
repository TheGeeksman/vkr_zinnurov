from django.urls import path, include
from .views import index, dashboard, examples, author

urlpatterns = [
    path('', index),
    path('dashboard/', dashboard, name='dashboard'),
    path('examples/', examples, name='examples_list'),
    path('author/', author, name='aboutauthor')
]
