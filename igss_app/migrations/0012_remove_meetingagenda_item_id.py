# Generated by Django 2.1.2 on 2018-12-17 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('igss_app', '0011_meetingagenda_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingagenda',
            name='item_id',
        ),
    ]