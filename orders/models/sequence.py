from django.db import models


# Secuencia 1 -> generar el codigo unico en mi orden SP000001
# Secuencia 2 -> generar el codigo unico en mi orden SP000002


class SequenceModel(models.Model):
    current = models.BigIntegerField(default=0, verbose_name="Secuencia actual")

    created_at = models.DateTimeField(verbose_name="Fecha creacion", auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name="Fecha modificacion", blank=True, null=True)

    class Meta:
        verbose_name = "Secuencia"
        verbose_name_plural = "Secuencias"
        db_table = 'sequence'