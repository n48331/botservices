# Generated by Django 4.2.5 on 2024-06-06 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=20, unique=True)),
                ('asset_name', models.CharField(max_length=255)),
                ('asset_category', models.CharField(max_length=50)),
                ('campaign_type', models.CharField(max_length=50)),
                ('project_type', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('csm', models.CharField(max_length=100)),
                ('pmo', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='scbot_api.project')),
            ],
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sender', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communications', to='scbot_api.project')),
            ],
        ),
    ]
