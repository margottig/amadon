# Generated by Django 3.2.4 on 2021-07-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorly_coded_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='orders', to='poorly_coded_store.Product'),
        ),
    ]
