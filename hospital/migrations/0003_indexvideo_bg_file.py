# Generated by Django 3.1.2 on 2020-11-24 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20201124_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexvideo',
            name='bg_file',
            field=models.ImageField(null=True, upload_to='hospital/videos', verbose_name='Background image '),
        ),
    ]
