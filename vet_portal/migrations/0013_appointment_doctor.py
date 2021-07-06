# Generated by Django 3.2.5 on 2021-07-06 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vet_portal', '0012_doctor_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='vet_portal.doctor'),
            preserve_default=False,
        ),
    ]
