# Generated by Django 2.2 on 2019-06-05 19:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_author_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(default='Demo content'),
            preserve_default=False,
        ),
    ]
