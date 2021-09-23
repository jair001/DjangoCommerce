from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# VBF vista basada en funcion
def catalogue(request):
    # TODO: logic
    title: str = "Empresa online"
    return render(request, 'catalogue/index.html', {"title_b": title})

# VBC vista basada en clase