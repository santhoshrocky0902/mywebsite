# Generated by Django 3.1.7 on 2021-04-02 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0019_hyperlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='hyperlink',
            name='facility_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='college.main_facility'),
        ),
    ]