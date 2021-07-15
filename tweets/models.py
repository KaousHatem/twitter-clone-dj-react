from django.db import models
import random

from django.conf import settings



User = settings.AUTH_USER_MODEL

# Create your models here.

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    # id = models.AutoField(True)
    parent = models.ForeignKey("self",null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="tweets")
    likes = models.ManyToManyField(User, related_name='tweet_user',blank=True, through=TweetLike)
    content = models.TextField(blank=True,null=True)
    image = models.FileField(upload_to='images/',blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']


    @property
    def is_retweet(self):
        return self.parent != None
    