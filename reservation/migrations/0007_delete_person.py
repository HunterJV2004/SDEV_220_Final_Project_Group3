# Generated by Django 5.0.7 on 2024-07-28 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_alter_appointment_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
