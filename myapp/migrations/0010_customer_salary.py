# Generated by Django 3.0.3 on 2020-03-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='salary',
            field=models.FloatField(null=True),
        ),
    ]
