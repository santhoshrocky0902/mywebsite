# Generated by Django 3.1.7 on 2021-04-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0009_auto_20210422_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mci_subcatagory',
            name='document_pdf',
            field=models.FileField(blank=True, default=None, null=True, upload_to='mci'),
        ),
    ]