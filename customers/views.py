# from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.contrib import messages

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
            customer = CustomerModel()
            customer.full_name = data.get('full_name')
            customer.dni = data.get('dni')
            customer.save()
            messages.success(request, "Registro Guardado")
            # redirect redirecciona a un html, junto con reverese_lazy, el parametro es el nombre de la app y la clase a la q quiere que vaya de views
            return redirect(reverse_lazy("customers:customers_list"))
            # print("Registro Guardado")
        else:
            messages.error(request, "Error al registrar")
            # print("Error")
    return render(request, "customers/create.html", {"form": form})
