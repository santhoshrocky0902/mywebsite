# Generated by Django 3.1.2 on 2020-11-19 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='picture',
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default=None, upload_to='news'),
        ),
    ]