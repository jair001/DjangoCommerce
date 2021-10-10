from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# al poner como parametro request indica que es controlador
from django.urls import reverse_lazy


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("login-username")
        password = request.POST.get("login-password")
        user =authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido {user.username}")
            # redirect redirecciona, envía, reverse_lazy dado 1 parametro identifica la url
            return redirect(reverse_lazy("catalogue:catalogue_home"))
        else:
            messages.error(request, "Credenciales incorrectas")

    return render(request, "users/login.html", {})


def logout_view(request):
    logout(request)
    messages.success(request, "Hasta pronto")
    return redirect(reverse_lazy("catalogue:catalogue_home"))