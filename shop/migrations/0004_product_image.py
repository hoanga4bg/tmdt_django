# Generated by Django 3.2.3 on 2021-05-31 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='', max_length=100),
        ),
    ]
