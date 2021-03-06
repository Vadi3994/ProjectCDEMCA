# Generated by Django 2.2.5 on 2019-12-15 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0002_auto_20191215_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('venue', models.CharField(max_length=120)),
                ('manager', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
