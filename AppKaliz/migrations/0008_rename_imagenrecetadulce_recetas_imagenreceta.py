# Generated by Django 4.1.7 on 2023-04-03 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppKaliz', '0007_recetas_delete_alfajor_delete_alfajores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recetas',
            old_name='imagenRecetaDulce',
            new_name='imagenReceta',
        ),
    ]