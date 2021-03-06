# Generated by Django 3.1.7 on 2021-04-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0008_mci_subcatagory_mci_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mci',
            name='document_pdf',
            field=models.FileField(blank=True, default=None, upload_to='mci'),
        ),
        migrations.AlterField(
            model_name='mci',
            name='href',
            field=models.URLField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='mci_subcatagory',
            name='document_pdf',
            field=models.FileField(blank=True, default=None, upload_to='mci'),
        ),
        migrations.AlterField(
            model_name='mci_subcatagory',
            name='href',
            field=models.URLField(blank=True, default=None),
        ),
    ]
