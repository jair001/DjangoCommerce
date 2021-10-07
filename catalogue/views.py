from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# MOdels
from catalogue.models import CategoryModel
from catalogue.models import ItemModel


# VBF vista basada en funcion
def index(request):
    # TODO: logic
    title: str = "Empresa online"

    categories = CategoryModel.objects.order_by('name')  # Lista categorias ordenadas por nombre
    items = ItemModel.objects.filter(stock=True).order_by('name')  # Lista de productos en stock
    return render(request, 'catalogue/index.html', {"title_b": title, "categories": categories, "items": items})

def category_items(request, category_slug=None):
    # Envía excepción si no encuentra o una instancia de objeto q ser+ia el registro de nuestra base en este caso una categoría
    category = get_object_or_404(CategoryModel, code=category_slug)
    filtered_items = ItemModel.objects.filter(category=category)    # lista de items x categoria

    if filtered_items.exists():
        message="Si existe"
        flag=True
    else:
        message = "no existe"
        flag=False
    return render(request, '', {"filtered_items": filtered_items, "flag": flag, "message": message})
# VBC vista basada en clase