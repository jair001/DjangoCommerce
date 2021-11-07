""""""
import datetime
import uuid

from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from orders.models.sequence import SequenceModel


class OrderModel(models.Model):
    ORDER_TRACKING_STATUS = (
        (1, "Procesada"),
        (2, "Enviada"),
        (3, "Pagada"),
        (4, "Completada"),
        (5, "Cancelada")
    )
    ORDER_PAYMENT_MODE = (
        (1, 'Efectivo'),
        (2, 'Deposito o transferencia'),
        (3, 'Tarjeta de crédito')
    )
    code = models.CharField(
        verbose_name="Código Transacción",
        unique=True,
        db_index=True,
        help_text="Código único de la transacción",
        max_length=60
    )  # MS000001
    date_emi = models.DateTimeField(
        verbose_name="Fecha Emisión",
        help_text="Fecha de emisión de la transacción"
    )
    customer = models.ForeignKey(
        "customers.CustomerModel",
        on_delete=models.PROTECT,
        help_text="Cliente",
        related_name="customer_orders", verbose_name="Cliente"
    )
    billing_address = models.CharField(
        verbose_name="Dirección", help_text="Dirección de facturación", max_length=220)
    shipping_address = models.CharField(verbose_name="Dirección Entrega", help_text="Dirección de entrega",
                                        max_length=220)

    tracking_status = models.IntegerField(
        choices=ORDER_TRACKING_STATUS,
        default=1,
        verbose_name="Estado de la orden"
    )
    payment_mode = models.IntegerField(
        choices=ORDER_PAYMENT_MODE,
        default=1,
        verbose_name="Forma de pago"
    )
    subtotal_base_0 = models.DecimalField(
        default=0, max_digits=9, decimal_places=2, verbose_name="Base 0", help_text="Subtotal base 0"
    )
    subtotal_base_12 = models.DecimalField(
        default=0, max_digits=9, decimal_places=2, verbose_name="Base 12", help_text="Subtotal base 12"
    )
    subtotal = models.DecimalField(
        default=0, max_digits=9, decimal_places=2, verbose_name="Sub Total", help_text="Subtotal"
    )
    tax_shipping = models.DecimalField(
        default=0, max_digits=6, decimal_places=2, verbose_name="Impuesto o fee para el envío.",
        blank=True
    )
    tax_12 = models.DecimalField(
        default=0, max_digits=9, decimal_places=2, verbose_name="IVA 12"
    )
    total = models.DecimalField(
        default=0, verbose_name="Total", help_text="Total del orden.", max_digits=9, decimal_places=2
    )
    total_items = models.IntegerField(
        verbose_name="Total de items",
        help_text="Catntidad de items en la orden.",
        default=0,
        blank=True
    )

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Órdenes"
        db_table = "order"

    def __str__(self):
        return f"{self.code}"


# colocar una señal (signal), la funcion es pasar un evento a un archivo
# pre_save es el metodo, sender es quien va a ser afectado con pre_save
# antes de guardar va a hacer algo en OrderModel
@receiver(pre_save, sender=OrderModel)
def set_code(sender, instance, **kwargs):
    index = 0
    sequence = SequenceModel.objects.all().first()
    if sequence:
        index = sequence.current +1
        sequence.current = index
        sequence.save(update_fields=['current'])
    reference = str(index)
    end_code = f"DC{reference.zfill(4)}"  # -> DC1, DC2...
    instance.code = end_code

@receiver(post_save, sender=OrderModel)
def notification_email(sender, instance, **kwargs):
    # instance.customer.email
    # email = "rnoboa22@gmail.com"
    email = "jair001@hotmail.com"
    subject, from_email, to = 'Notificacion de Orden', 'admin@mitienda.com', email
    text_content = f'Order creada exitosamente.'
    html_content = f'<p>{instance.code}, gracias por tu compra.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
