from django.urls import path

from customers.views import customers_list, customers_create

app_name = 'customers'
urlpatterns = (
    path('', customers_list, name="customers_list"),
    path('create/', customers_create, name="customers_create"),
)