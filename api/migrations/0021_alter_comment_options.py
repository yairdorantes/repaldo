# Generated by Django 4.1.1 on 2022-10-14 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_post_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-id']},
        ),
    ]
