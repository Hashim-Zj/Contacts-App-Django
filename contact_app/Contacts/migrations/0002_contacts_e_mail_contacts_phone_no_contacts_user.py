# Generated by Django 5.1 on 2024-08-12 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='e_mail',
            field=models.CharField(default=2, max_length=60, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacts',
            name='phone_no',
            field=models.CharField(default=2, max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacts',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
