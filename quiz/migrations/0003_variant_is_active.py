# Generated by Django 4.2.1 on 2023-05-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_lesson_options_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
