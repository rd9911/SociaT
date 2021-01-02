import random

from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # to add feature that will inform retweets that tweet was deleted: null=True, SET_NULL
    like = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.content

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'likes': random.randint(1, 100)
        }

