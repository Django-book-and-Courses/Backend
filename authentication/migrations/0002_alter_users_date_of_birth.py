# Generated by Django 5.0.4 on 2024-04-21 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
