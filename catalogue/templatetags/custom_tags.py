from django import template

from catalogue.models import CategoryModel

register = template.Library()


@register.inclusion_tag('catalogue/templatetags/categories.html', takes_context=True)
def categories_menu():
    categories = CategoryModel.objects.order_by('name')
    return {"categories": categories}
