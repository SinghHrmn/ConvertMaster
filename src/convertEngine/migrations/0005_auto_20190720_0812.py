# Generated by Django 2.2 on 2019-07-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convertEngine', '0004_myconversion_convname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myconversion',
            name='converted',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='myconversion',
            name='original',
            field=models.CharField(max_length=4),
        ),
    ]
