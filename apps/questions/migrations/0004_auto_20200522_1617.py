# Generated by Django 3.0.6 on 2020-05-22 16:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0003_auto_20200520_2309'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='response',
            unique_together={('choices', 'user')},
        ),
    ]