# Generated by Django 5.0.3 on 2024-03-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]