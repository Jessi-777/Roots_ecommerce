# Generated by Django 4.0.2 on 2022-03-08 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_current_date_product_modified_date_variation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=700),
        ),
    ]
