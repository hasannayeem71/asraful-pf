# Generated by Django 3.2 on 2021-05-23 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_recentproject_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentproject',
            name='Picture',
            field=models.ImageField(default=2, upload_to='pics'),
            preserve_default=False,
        ),
    ]
