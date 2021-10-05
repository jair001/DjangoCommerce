# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from customers.forms import BasicCustomerForm
from customers.models import CustomerModel


# LISTAR
def customers_list(request):
    customers = CustomerModel.objects.filter(status=True).order_by("full_name")
    # return HttpResponse("Lista de clientes") # response devuelve un mensaje, render puede gestionar una plantilla
    # parametros: lo que recibe, plantilla, contexto, contexto es la información del controlador hacia la presentación
    return render(request, "customers/list.html", {"customers": customers})


# CREAR
def customers_create(request):
    form = BasicCustomerForm()
    # captura la info del formulario, si el request fue desde un post:
    if request.method == "POST":
        form = BasicCustomerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data # devuelve un diccionario dict {"full_name": <>, "dni": <>}
        else:
            print("Error")
    return render(request, "customers/create.html", {"form": form})
