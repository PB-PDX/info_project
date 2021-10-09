# Generated by Django 3.2.8 on 2021-10-09 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='federalregister',
            name='id',
        ),
        migrations.AlterField(
            model_name='federalregister',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='federalregister',
            name='pubDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='federalregister',
            name='title',
            field=models.CharField(max_length=500, primary_key=True, serialize=False, unique=True),
        ),
    ]
