import admin_thumbnails
from django.contrib import admin
from catalogue.models import ItemModel, CategoryModel


@admin.register(ItemModel)
@admin_thumbnails.thumbnail('photo', 'Thumbnail')
class ItemModelAdmin(admin.ModelAdmin):
    search_fields = ("name", "sku")
    list_display = ("name", "photo_thumbnail", "pvp", "description")
    list_filter = ("category", "pvp", "stock")
    raw_id_fields = ("category",)
    fields = ("name", "sku", "pvp", "category", "photo", "stock", "description")

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ("name", "code")
    list_display = ("name", "code")

