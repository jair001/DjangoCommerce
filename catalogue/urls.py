from django.urls import path

from catalogue.views import index, item_detail

app_name = 'catalogue'
urlpatterns = [
    # path('catalogo/', catalogue, name='catalogue'),
    path('', index, name='catalogue_home'),
    path('item/<int:id>/', item_detail, name='item_detail'),
]