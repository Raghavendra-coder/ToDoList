# Generated by Django 3.2.5 on 2021-07-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet_portal', '0005_alter_doctor_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.CharField(default='abc@gmail.com', max_length=30),
            preserve_default=False,
        ),
    ]
