# Generated by Django 5.0.1 on 2024-02-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.IntegerField(default='00000'),
            preserve_default=False,
        ),
    ]