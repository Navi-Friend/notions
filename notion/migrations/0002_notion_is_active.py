# Generated by Django 5.1.1 on 2024-10-03 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notion',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
