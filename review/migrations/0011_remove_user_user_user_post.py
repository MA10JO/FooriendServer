# Generated by Django 4.1.3 on 2022-12-04 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0010_remove_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.post'),
        ),
    ]
