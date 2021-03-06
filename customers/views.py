# from django.http import HttpResponse
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction

from customers.forms import BasicCustomerForm
from customers.models import CustomerModel


# LISTAR

# @login_required()
def customers_list(request):
    customers = CustomerModel.objects.filter(status=True).order_by("full_name")
    # return HttpResponse("Lista de clientes") # response devuelve un mensaje, render puede gestionar una plantilla
    # parametros: lo que recibe, plantilla, contexto, contexto es la información del controlador hacia la presentación
    return render(request, "customers/list.html", {"customers": customers})


# OBTENER
# @login_required() indica antes de cada funcion, que requiere estar logueado, se coloca antes de cada funcion
# login_url redirecciona
@login_required(login_url='/security/login')
def customer_detail(request, identifier: int):
    # el campo identifier se pasa a las urls
    try:
        customer = CustomerModel.objects.get(id=identifier)
    except CustomerModel.DoesNotExist:
        customer = None

    return render(request, "customers/detail.html", {"customer": customer})


# CREAR
@login_required(login_url='/security/login')
def customers_create(request):
    form = BasicCustomerForm()
    # captura la info del formulario, si el request fue desde un post:
    if request.method == "POST":
        form = BasicCustomerForm(request.POST)
        if form.is_valid():
            with transaction.commit():
                data = form.cleaned_data # devuelve un diccionario dict {"full_name": <>, "dni": <>}
                customer = CustomerModel()
                customer.full_name = data.get('full_name')
                customer.dni = data.get('dni')
                customer.created_by = request.user
                customer.save()
                # se puede guardar con una sola linea
                # CustomerModel.objects.create(full_name=data.get('full_name'), dni=data.get('dni'))
                messages.success(request, "Registro Guardado")
                # redirect redirecciona a un html, junto con reverese_lazy, el parametro es el nombre de la app y la clase a la q quiere que vaya de views
                return redirect(reverse_lazy("customers:customers_list"))
                # print("Registro Guardado")
        else:
            messages.error(request, "Error al registrar")
            # print("Error")
    return render(request, "customers/create.html", {"form": form})


# ACTUALIZAR
@login_required(login_url='/security/login')
def customers_edit(request, identifier: int):
    # 1. Obtener registro a editar
    try:
        customer = CustomerModel.objects.get(id=identifier)
    except CustomerModel.DoesNotExist:
        customer = None

    form = BasicCustomerForm()
    if customer is not None:
        form = BasicCustomerForm(initial={"full_name": customer.full_name, "dni": customer.dni})

        if request.method == "POST":
            form = BasicCustomerForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                customer.full_name = data.get("full_name")
                customer.dni = data.get("dni")
                customer.modified_at = datetime.now()
                customer.modified_by = request.user
                customer.save()
                messages.success(request,"Cliente modificado")
                return redirect(reverse_lazy("customers:customers_list"))
            else:
                messages.error(request, "Error al editar")
    return render(request, "customers/update.html", {"form": form})


# ELIMINAR
@login_required(login_url='/security/login')
def customers_delete(request, id: int):
    customer = get_object_or_404(CustomerModel, id=id, status=True)
    customer.deleted_at = datetime.now()
    customer.status = False
    customer.save()
    messages.success(request, "Cliente eliminado")
    return redirect(reverse_lazy("customers:customers_list"))