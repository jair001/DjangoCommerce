from django.urls import path

from customers.views import customers_list, customers_create, customer_detail, customers_edit, customers_delete

app_name = 'customers'
urlpatterns = (
    path('', customers_list, name="customers_list"),
    path('create/', customers_create, name="customers_create"),
    path('detail/<int:identifier>/', customer_detail, name='customers_detail'),
    path('edit/<int:identifier>/', customers_edit, name='customers_edit'),
    path('delete/<int:id>/', customers_delete, name='customers_delete')
)