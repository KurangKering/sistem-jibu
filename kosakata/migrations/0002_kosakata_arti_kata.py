# Generated by Django 3.2.1 on 2021-05-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kosakata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kosakata',
            name='arti_kata',
            field=models.CharField(default=None, max_length=100),
        ),
    ]