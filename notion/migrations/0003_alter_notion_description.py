# Generated by Django 5.1.1 on 2024-10-06 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notion', '0002_notion_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notion',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
