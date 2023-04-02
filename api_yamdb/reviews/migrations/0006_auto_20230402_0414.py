# Generated by Django 3.2 on 2023-04-02 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20230401_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.genre'),
        ),
        migrations.DeleteModel(
            name='GenreTitle',
        ),
    ]
