# Generated by Django 3.2.6 on 2021-08-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0005_alter_datastructure_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
