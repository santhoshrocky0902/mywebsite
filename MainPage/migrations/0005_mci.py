# Generated by Django 3.1.2 on 2020-12-01 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0004_auto_20201119_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='mci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=250)),
                ('document_pdf', models.FileField(default=None, upload_to='mci')),
            ],
        ),
    ]