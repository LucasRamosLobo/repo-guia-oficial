# Generated by Django 3.1 on 2023-02-09 20:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0009_auto_20230203_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='Nome'),
        ),
    ]