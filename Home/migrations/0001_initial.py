# Generated by Django 4.0.5 on 2024-06-05 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('faullname', models.CharField(max_length=20, null=True)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
    ]
