# Generated by Django 3.1.2 on 2021-06-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaWeb', '0006_auto_20210616_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen producto'),
        ),
    ]
