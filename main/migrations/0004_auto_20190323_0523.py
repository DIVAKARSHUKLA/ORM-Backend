# Generated by Django 2.1.7 on 2019-03-23 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190322_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranalysis',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
