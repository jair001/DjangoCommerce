from django.contrib import admin

from orders.models import SequenceModel


@admin.register(SequenceModel)
class SequenceAdmin(admin.ModelAdmin):
    list_display = ("current",)
