# Generated by Django 5.0.3 on 2024-05-23 00:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0010_alter_needhelp_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='needhelp',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour.tour'),
        ),
    ]
