# Generated by Django 2.0.3 on 2018-05-25 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_verified'),
        ('vacancy', '0007_auto_20180524_0816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='city',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='office',
            field=models.ManyToManyField(to='company.Office'),
        ),
    ]
