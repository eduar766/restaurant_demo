# Generated by Django 2.2 on 2019-05-10 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('is_video', models.BooleanField(default=False)),
            ],
        ),
    ]
