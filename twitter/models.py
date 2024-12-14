from django.db import models

# Create your models here.
# textbox, likes, retweets, comments
class Tweets(models.Model):
    tweet_body = models.TextField()
    likes = models.IntegerField()
    retweets = models.IntegerField()
    