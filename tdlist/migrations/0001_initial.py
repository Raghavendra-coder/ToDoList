# Generated by Django 3.2.5 on 2021-07-03 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('com_Date', models.DateField()),
                ('content', models.CharField(default='', max_length=50)),
            ],
        ),
    ]