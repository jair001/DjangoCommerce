"""
"""
from django.db import models


# Order -> item1, item2, item3

class OrderItem(models.Model):
    """
    order(rel), product, quantity, pvp
    """
    order = models.ForeignKey(
        "orders.OrderModel", on_delete=models.CASCADE, help_text="Orden", related_name="items"
    )
    item = models.ForeignKey(
        "catalogue.ItemModel", on_delete=models.PROTECT, verbose_name="Item"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    pvp = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Precio U.")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        db_table = "order_item"