# Generated by Django 3.2 on 2021-05-23 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentproject',
            name='projectcatagory',
            field=models.CharField(blank=True, choices=[('Web Design', 'Web Design'), ('web development', 'Web Development'), ('Wordpress', 'wordpress')], max_length=30, null=True),
        ),
    ]