# Generated by Django 3.2.2 on 2021-07-28 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0015_alter_intereses_aptitudes__subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intereses_aptitudes',
            old_name='_subcategory',
            new_name='subcategory',
        ),
        migrations.AlterField(
            model_name='skills_idiomas',
            name='knowledge_level',
            field=models.IntegerField(choices=[(1, 'Basico'), (2, 'Intermedio'), (3, 'Avanzado')], default=(1, 'Basico'), verbose_name='Nivel de conocimiento'),
        ),
    ]
