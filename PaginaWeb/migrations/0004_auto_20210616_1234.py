# Generated by Django 3.1.2 on 2021-06-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaWeb', '0003_auto_20210616_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagen', verbose_name='Imgamen producto'),
        ),
    ]
