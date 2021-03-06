# Generated by Django 3.2.3 on 2021-10-06 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=160, verbose_name='Nombre completo')),
                ('dni', models.CharField(help_text='No.Identificación Ej.CED, RUC', max_length=20, verbose_name='No.Identificación')),
                ('status', models.BooleanField(default=True, help_text='Estado Ej. activo => True, inactivo => False', verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificación')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de eliminación')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
            ],
        ),
    ]
