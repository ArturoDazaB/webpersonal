# Generated by Django 3.2.2 on 2021-06-06 17:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20210606_1339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='description',
            options={'ordering': ['-created'], 'verbose_name': 'Descripcion', 'verbose_name_plural': 'Descripcion'},
        ),
        migrations.AlterField(
            model_name='description',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Descripcion'),
        ),
    ]
