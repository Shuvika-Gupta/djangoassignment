# Generated by Django 4.0.5 on 2022-06-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_profile_delete_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default=123456, max_length=50),
            preserve_default=False,
        ),
    ]