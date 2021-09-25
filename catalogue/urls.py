from django.urls import path

from catalogue.views import index

app_name = 'catalogue'
urlpatterns = [
    # path('catalogo/', catalogue, name='catalogue'),
    path('', index, name='catalogue_home'),
]