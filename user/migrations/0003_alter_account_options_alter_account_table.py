# Generated by Django 4.0.4 on 2022-11-25 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_account_created_at_alter_account_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': '유저', 'verbose_name_plural': '유저'},
        ),
        migrations.AlterModelTable(
            name='account',
            table='account',
        ),
    ]
