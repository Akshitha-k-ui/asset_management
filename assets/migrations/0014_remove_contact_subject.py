# Generated by Django 5.1 on 2024-09-02 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0013_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]
