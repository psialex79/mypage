# Generated by Django 4.2 on 2024-02-14 06:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users_checker', '0002_follower_name_follower_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='follower',
            name='date_of_exclusion',
            field=models.DateField(blank=True, null=True),
        ),
    ]