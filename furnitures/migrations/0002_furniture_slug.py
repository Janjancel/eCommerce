# Generated by Django 4.2.16 on 2024-11-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
