# Generated by Django 3.0.7 on 2020-09-26 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ngo_requirements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='ngo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ngo_requirements.Ngo'),
        ),
    ]
