from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class CustomerModel(models.Model):
    full_name = models.CharField(max_length=160, verbose_name='Nombre completo')
    dni = models.CharField(max_length=20, verbose_name='No.Identificación',
                           help_text='No.Identificación Ej.CED, RUC')

    # Audit
    status = models.BooleanField(default=True, verbose_name='Estado',
                                help_text='Estado Ej. activo => True, inactivo => False')
    created_by = models.ForeignKey(
        User, verbose_name='Creado por', on_delete=models.SET_NULL, null=True, related_name='created')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    modified_by = models.ForeignKey(
        User, verbose_name='Modificado por', on_delete=models.SET_NULL, null=True, related_name='modified')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación', null=True, blank=True)
    deleted_at = models.DateTimeField(verbose_name='Fecha de eliminación', null=True, blank=True)

class Meta:
    verbose_name = "Customer"
    verbose_name_plural = "Customers"
    db_table = "customer"

def __str__(self):
    return f"[{self.dni}] {self.full_name}"
