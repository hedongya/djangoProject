# Generated by Django 2.1.4 on 2019-01-06 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='keyword1',
            field=models.CharField(default='', max_length=50),
        ),
    ]