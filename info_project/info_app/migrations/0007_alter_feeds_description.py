# Generated by Django 3.2.8 on 2021-10-20 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0006_alter_feeds_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
