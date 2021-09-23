from django.db import modelsclass CategoryModel(models.Model):    # id no es necesario xq crea automatico    code = models.CharField(max_length=80, verbose_name="Codigo", unique=True, blank=True)    name = models.CharField(max_length=150, verbose_name="Nombre", help_text="Nombre de la Categoria.")    description = models.TextField(verbose_name="Descripcion", help_text="Descripcion de la Catehoria.", blank=True)    class Meta:        ordering = ['-name']    # orden descendente por name        verbose_name = "Categoría"        verbose_name_plural = "Categorías"        db_table = "category"    def __str__(self) -> str:        return f"{self.name}"class ItemModel(models.Model):    # on_delete=models.CASCADE    # on_delete=models.PROTECT si borra uno, otro se mantiene    # # on_delete=models.SET_NULL si borra uno, otro se pone NULL    category = models.ForeignKey(        CategoryModel, on_delete=models.SET_NULL, help_text="relacion con categoria",        related_name="items", blank=True, null=True    # nombre de la relación, permite crear item sin categoría    )    sku = models.CharField(max_length=150, verbose_name="Codigo", unique=True)    name = models.CharField(max_length=150, verbose_name="Nombre", help_text="Nombre del item.")    pvp = models.DecimalField(max_digits=9, decimal_places=3, verbose_name="Precio",                              help_text="Precio de venta con IVA")    photo = models.ImageField(upload_to="item/", verbose_name="Foto", help_text="Foto principal del item.", blank=True)    description = models.TextField(verbose_name="Descripción", help_text="Descripción del item.", blank=True,                                   default="")    stock = models.BooleanField(default=True, verbose_name="Stock")    # Nombrar el objeto    def __str__(self) -> str:        return f"[{self.sku}] {self.name}"    # personaliza la tabla    class Meta:        verbose_name = "Item"        verbose_name_plural = "Items"        db_table = "Item"   # pone el nombre a la tabla si no se pone crea como ItemModel    def delete(self, using=None, keep_parents=False):        pass         # TODO: implement soft delete# @receiver(pre_save, sender=ItemModel)# def set_code(sender, instance, **kwargs)#     ref = ItemModel.objects.all.last().pk + 1#     code = f'CODE - (ref)'#     instance.sku = code