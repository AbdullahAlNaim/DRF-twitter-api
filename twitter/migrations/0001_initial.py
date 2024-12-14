# Generated by Django 5.1.4 on 2024-12-14 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_body', models.TextField()),
                ('likes', models.IntegerField()),
                ('retweets', models.IntegerField()),
            ],
        ),
    ]
