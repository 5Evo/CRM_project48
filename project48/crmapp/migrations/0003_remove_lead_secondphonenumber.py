# Generated by Django 4.1 on 2022-09-13 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='secondPhoneNumber',
        ),
    ]
