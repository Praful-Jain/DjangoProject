# Generated by Django 4.2.13 on 2024-06-06 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='no comment', max_length=40),
        ),
    ]