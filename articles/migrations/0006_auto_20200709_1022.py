# Generated by Django 3.0.5 on 2020-07-09 14:22

import articles.models
from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_attrs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='attrs',
            field=django_mysql.models.JSONField(default=articles.models.first),
        ),
    ]
