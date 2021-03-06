# Generated by Django 3.2.3 on 2021-09-21 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_categorymodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'ordering': ['-name'], 'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='category',
            field=models.ForeignKey(blank=True, help_text='relacion con categoria', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='catalogue.categorymodel'),
        ),
    ]
