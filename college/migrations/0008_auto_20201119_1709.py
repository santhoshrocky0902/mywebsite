# Generated by Django 3.1.2 on 2020-11-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_auto_20201119_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='brochure',
            field=models.FileField(blank=True, default=None, null=True, upload_to='brochure'),
        ),
    ]
