# Generated by Django 2.2.5 on 2019-12-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0005_auto_20191216_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]