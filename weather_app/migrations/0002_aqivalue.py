# Generated by Django 5.1.1 on 2025-02-06 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AQIValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
