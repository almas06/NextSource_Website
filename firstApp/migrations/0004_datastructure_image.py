# Generated by Django 3.2.6 on 2021-08-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_datastructure'),
    ]

    operations = [
        migrations.AddField(
            model_name='datastructure',
            name='image',
            field=models.ImageField(default='static/dsa1.jpg', upload_to='images'),
        ),
    ]
