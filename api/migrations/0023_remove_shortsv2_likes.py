# Generated by Django 4.1.1 on 2022-10-14 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_post_image_src'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortsv2',
            name='likes',
        ),
    ]
