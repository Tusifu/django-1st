# Generated by Django 3.0.5 on 2020-05-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200501_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='walk.jpg', upload_to=''),
        ),
    ]
