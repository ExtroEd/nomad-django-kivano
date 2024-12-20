# Generated by Django 5.1.3 on 2024-11-09 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='article',
            field=models.CharField(default=10000, editable=False, max_length=6, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.CharField(choices=[('На складе', 'На складе'), ('Уточняйте наличие', 'Уточняйте наличие')], default='Уточняйте наличие', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='free_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='reviews_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.CharField(default='нет', max_length=50),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='catalog.product')),
            ],
        ),
    ]
