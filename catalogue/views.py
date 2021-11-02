from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# MOdels
from catalogue.models import CategoryModel
from catalogue.models import ItemModel


# VBF vista basada en funcion, existen otras # VBC vista basada en clase
def index(request):
    # TODO: logic
    title: str = "Empresa online"

    items = ItemModel.objects.filter(stock=True).order_by('name')  # Lista de productos en stock
    categories = CategoryModel.objects.order_by('name')  # Lista categorias ordenadas por nombre

    # parametro que viene desde el buscador del formulario
    param = request.GET.get("search", None)    # si el parametro search está vacio, ponga None
    param_category = request.GET.get("search-category", None)
    if param or param_category:
        # Q permite realizar consultas por campos, ver djanjo queries Q
        # __ indica que accede a un metodo o campo
        # | significa or, and es la coma cuando se usa Q
        items = items.filter(
            Q(name__icontains=param) |
            Q(category__name__icontains=param) |
            Q(category__pk__exact=int(param_category))
        )

    return render(request, 'catalogue/index.html', {"categories": categories, "items": items})

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


def item_detail(request, id:int):
    try:
        item = ItemModel.objects.get(id=id)
    except ItemModel.DoesNotExist:
        item = None

    return render(request, "catalogue/item_detail.html", {"item": item})

