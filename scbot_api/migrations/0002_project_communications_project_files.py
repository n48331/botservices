# Generated by Django 4.2.5 on 2024-06-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scbot_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Communications',
            field=models.ManyToManyField(related_name='projects', to='scbot_api.communication'),
        ),
        migrations.AddField(
            model_name='project',
            name='Files',
            field=models.ManyToManyField(related_name='projects', to='scbot_api.file'),
        ),
    ]
