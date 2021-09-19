from django.urls import path

from catalogue.views import catalogue

app_name = 'catalogue'
urlpatterns = [
    path('catalogo/', catalogue, name='catalogue'),
]