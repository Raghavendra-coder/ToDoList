# Generated by Django 3.2.5 on 2021-07-06 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet_portal', '0004_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(),
        ),
    ]
