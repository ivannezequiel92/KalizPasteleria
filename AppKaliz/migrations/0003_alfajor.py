# Generated by Django 4.1.7 on 2023-03-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppKaliz', '0002_alfajores_clientes_tortas_delete_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alfajor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=30)),
                ('sabor', models.CharField(max_length=30)),
            ],
        ),
    ]