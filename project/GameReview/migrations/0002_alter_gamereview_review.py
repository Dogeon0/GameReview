# Generated by Django 5.0.6 on 2024-05-23 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameReview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamereview',
            name='review',
            field=models.TextField(max_length=1500),
        ),
    ]
