# Generated by Django 4.2 on 2024-02-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_checker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='follower',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]