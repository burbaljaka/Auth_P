# Generated by Django 3.0 on 2019-12-13 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacebookGoogleAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
