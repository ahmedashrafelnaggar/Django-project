# Generated by Django 5.0.1 on 2024-01-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watcher',
            name='watch',
            field=models.ManyToManyField(related_name='watch', to='pages.vedio'),
        ),
    ]
