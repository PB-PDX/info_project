# Generated by Django 3.2.8 on 2021-10-16 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_feeds'),
        ('info_app', '0003_alter_feeds_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='subscriber',
            field=models.ManyToManyField(to='users.Profile'),
        ),
    ]