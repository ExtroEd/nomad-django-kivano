# Generated by Django 4.2.17 on 2025-01-17 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_skip_recaptcha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='skip_recaptcha',
        ),
    ]
