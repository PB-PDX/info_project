# Generated by Django 3.2.8 on 2021-10-10 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FederalRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, unique=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('pubDate', models.DateField(null=True)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
