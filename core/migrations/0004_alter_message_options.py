# Generated by Django 4.1.7 on 2023-03-15 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_room_options_room_partcipants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
