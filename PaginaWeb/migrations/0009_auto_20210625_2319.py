# Generated by Django 3.1.2 on 2021-06-26 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaWeb', '0008_auto_20210616_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='instrumentos'),
        ),
    ]