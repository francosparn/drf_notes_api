# Generated by Django 4.2.6 on 2023-11-04 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
