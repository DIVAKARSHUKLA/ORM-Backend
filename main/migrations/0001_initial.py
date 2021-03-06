# Generated by Django 2.1.7 on 2019-03-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.TextField(max_length=30)),
                ('name', models.TextField(max_length=50)),
                ('tweet_positive', models.FloatField()),
                ('tweet_negative', models.FloatField()),
                ('tweet_neutral', models.FloatField()),
                ('reply_positive', models.FloatField()),
                ('reply_negative', models.FloatField()),
                ('reply_neutral', models.FloatField()),
            ],
        ),
    ]
