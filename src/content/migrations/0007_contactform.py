# Generated by Django 2.2 on 2019-06-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
