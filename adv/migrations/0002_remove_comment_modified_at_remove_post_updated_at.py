# Generated by Django 4.1.3 on 2022-11-26 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
    ]
