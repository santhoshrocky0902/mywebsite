# Generated by Django 3.1.7 on 2021-04-03 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0025_markdetails_some_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='markdetails',
            name='another_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='college.twelthdetails'),
        ),
    ]