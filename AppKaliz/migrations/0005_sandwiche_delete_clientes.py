# Generated by Django 4.1.7 on 2023-03-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppKaliz', '0004_torta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sandwiche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('sabor', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
    ]
